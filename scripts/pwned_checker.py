#!/usr/bin/env python3
"""
pwned_checker.py
================

Checks whether a password has appeared in known data breaches, using the
free "Pwned Passwords" API from Have I Been Pwned (haveibeenpwned.com).

THE KEY IDEA: k-ANONYMITY
-------------------------
We never send your password, or even its full hash, over the internet.

1. We hash the password with SHA-1, giving a 40-character hex string,
   e.g.  5BAA61E4C9B93F3F0682250B6CF8331B7EE68FD8
2. We send ONLY the first 5 characters ("5BAA6") to the API.
3. The API returns every breached hash suffix that starts with that prefix
   (usually several hundred of them), each with a count of how many times
   it was seen in breaches.
4. We search that list LOCALLY for the remaining 35 characters.

The server only ever learns "someone asked about one of ~800 hashes
starting with 5BAA6". It cannot tell which one, so it cannot know your
password. This pattern is called k-anonymity, and it is a classic example
of privacy-preserving security design.

HOW TO RUN (on macOS)
---------------------
    python3 pwned_checker.py

It uses only Python's standard library, so there is nothing to install.
Type a password when prompted (it will not be shown on screen), and press
Enter on an empty line to quit.

ETHICS NOTE
-----------
Only check your own passwords. Never collect or test other people's.
"""

# ---------------------------------------------------------------------------
# IMPORTS
# ---------------------------------------------------------------------------

import hashlib          # Built-in hashing functions (SHA-1, SHA-256, MD5...)
import getpass          # Reads input without echoing it to the screen
import sys              # Lets us exit the program cleanly
import urllib.request   # Makes HTTP requests using only the standard library
import urllib.error     # Exception types for network errors


# ---------------------------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------------------------

# The "range" endpoint: we append a 5-character hash prefix to this URL.
API_URL = "https://api.pwnedpasswords.com/range/"

# The API asks every client to identify itself with a User-Agent header.
# Requests without one may be rejected.
USER_AGENT = "pwned-checker-learning-script"


# ---------------------------------------------------------------------------
# STEP 1: HASH THE PASSWORD
# ---------------------------------------------------------------------------

def sha1_hash(password: str) -> str:
    """
    Return the SHA-1 hash of a password as an UPPERCASE hex string.

    - .encode("utf-8") converts the text into bytes, because hash
      functions work on bytes, not on Python strings.
    - hashlib.sha1(...) runs the SHA-1 algorithm over those bytes.
    - .hexdigest() turns the 20-byte result into 40 hex characters.
    - .upper() matches the API, which returns hashes in uppercase.

    Note: SHA-1 is considered broken for things like digital signatures,
    and should NEVER be used to store passwords in a real system (use
    bcrypt, scrypt or Argon2 for that). Here it is only used as a lookup
    key, because that is the format the HIBP dataset is published in.
    """
    return hashlib.sha1(password.encode("utf-8")).hexdigest().upper()


# ---------------------------------------------------------------------------
# STEP 2: ASK THE API FOR ALL HASHES SHARING OUR PREFIX
# ---------------------------------------------------------------------------

def fetch_hash_suffixes(prefix: str) -> str:
    """
    Send the 5-character prefix to the API and return its raw text reply.

    The reply looks like this, one entry per line:

        0018A45C4D1DEF81644B54AB7F969B88D65:10
        00D4F6E8FA6EECAD2A3AA415EEC418D38EC:2
        ...

    Each line is   <35-char hash suffix>:<times seen in breaches>
    """
    url = API_URL + prefix

    # Build the request and attach headers.
    # "Add-Padding: true" asks the server to add fake entries (with a count
    # of 0) so that the SIZE of the response does not leak information to
    # anyone watching the network traffic. A nice extra privacy touch.
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Add-Padding": "true",
        },
    )

    # 'with' makes sure the connection is closed when we are done.
    # timeout=10 stops the script hanging forever if the network is down.
    with urllib.request.urlopen(request, timeout=10) as response:
        # The response arrives as bytes, so we decode it into text.
        return response.read().decode("utf-8")


# ---------------------------------------------------------------------------
# STEP 3: SEARCH THE REPLY LOCALLY FOR OUR FULL HASH
# ---------------------------------------------------------------------------

def count_breaches(suffix: str, response_text: str) -> int:
    """
    Look through the API reply for our 35-character suffix.

    Returns how many times the password appeared in breaches,
    or 0 if it was not found.
    """
    # splitlines() breaks the big block of text into a list of lines.
    for line in response_text.splitlines():
        # Each line is "SUFFIX:COUNT". split(":") separates the two parts.
        hash_suffix, count = line.split(":")

        # If this suffix matches ours, we have found our password.
        if hash_suffix == suffix:
            return int(count)

    # We checked every line and found no match.
    return 0


# ---------------------------------------------------------------------------
# PUTTING IT TOGETHER
# ---------------------------------------------------------------------------

def check_password(password: str) -> int:
    """Run the full k-anonymity check and return the breach count."""
    full_hash = sha1_hash(password)

    # Slice the hash: first 5 characters go to the API,
    # the other 35 stay on your machine.
    prefix = full_hash[:5]
    suffix = full_hash[5:]

    response_text = fetch_hash_suffixes(prefix)
    return count_breaches(suffix, response_text)


def main() -> None:
    """Prompt for passwords in a loop and report the results."""
    print("Pwned Passwords checker")
    print("Your password is hashed locally; only 5 hash characters are sent.")
    print("Press Enter on an empty line to quit.\n")

    while True:
        # getpass hides what you type, like a real login prompt.
        password = getpass.getpass("Password to check: ")

        # An empty entry means the user wants to stop.
        if not password:
            print("Goodbye.")
            sys.exit(0)

        try:
            count = check_password(password)
        except urllib.error.HTTPError as error:
            # The server replied, but with an error code (e.g. 429 = too many requests).
            print(f"  API error: HTTP {error.code}. Try again in a moment.\n")
            continue
        except urllib.error.URLError as error:
            # We could not reach the server at all (no internet, DNS issue,
            # or SSL certificate problem; see the note in the chat).
            print(f"  Network error: {error.reason}\n")
            continue

        # Report the result. The :, inside the f-string adds thousands
        # separators, so 3730471 prints as 3,730,471.
        if count:
            print(f"  FOUND in breaches {count:,} times. Do not use this password.\n")
        else:
            print("  Not found in known breaches. (That does not guarantee it is strong.)\n")


# This line means: only run main() if the file is executed directly,
# not if it is imported into another script as a module.
if __name__ == "__main__":
    main()