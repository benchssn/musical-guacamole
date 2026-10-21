
import base64

def decode_base64(encoded_text):
    try:
        decoded = base64.b64decode(encoded_text, validate=True)
        return decoded.decode("utf-8")
    except (ValueError, UnicodeDecodeError) as e:
        return f"Decoding error: {e}"

# User input
encoded_text = input("Enter Base64 string: ")

# Decode and display
print("Decoded:", decode_base64(encoded_text))