# NFC

Near field communication (NFC) lets two devices, such as a phone and a payment terminal, exchange data when they are very close. It is the technology behind tap-to-pay. The article is a Square publication, so it also promotes Square’s contactless readers and Tap to Pay on iPhone.

**How it works**

- NFC is a subset of RFID. It was introduced in the early 2000s and runs at 13.56 MHz.
- The device must be within about two inches of the reader. The two exchange encrypted data and the payment finishes in seconds.
- It is used for building access cards as well as payments. Apple Pay, Google Pay (the article calls it “Android Pay” in one place) and Samsung Pay are the main payment apps.

**Setup on phones**

|  | iPhone | Android |
| --- | --- | --- |
| Compatibility | iPhone 7 or newer, iOS 13+ | Most modern NFC-equipped phones (Samsung, Pixel, Xiaomi, Huawei) |
| Enable | Payments work automatically. For tags, add “NFC Tag Reader” in Control Center. | Settings > Connected Devices/Connections > Connection Preferences > toggle NFC on |
| Payments | Apple Pay via Wallet, authenticated by Face ID, Touch ID or passcode | Google Pay or similar, authenticated by PIN, fingerprint or face |
| Scan tags | Open the Control Center reader and hold the phone near the tag | Hold the phone near the tag with NFC on |
| Automation | Shortcuts app | Tasker or NFC Tools |
| File sharing | Not mentioned | Android Beam, “if available” |

**Troubleshooting:** Check that NFC is on, restart the phone, remove cases and metal objects, update the software, test another tag or device, and reset network settings. If none of that works, contact Apple or the phone maker.

**NFC tags**

Tags are small passive devices powered by the phone’s field. They store a link, contact details or a command. Common uses are:

- contactless payments
- smart home control
- sharing Wi-Fi details or contacts
- access control for doors and cars
- transit fares
- verifying luxury goods or pharmaceuticals
- phone automations such as silent mode

**Security**

- Magnetic-stripe data is static. NFC data is encrypted and changes with each transaction.
- Apple Pay uses tokenization. The bank swaps your card details for a random token, so the phone never holds usable card data, and the token changes with each transaction.
- Payments need biometrics or a passcode, so a stolen phone is of little use to a thief.

**EMV vs NFC**

|  | EMV | NFC |
| --- | --- | --- |
| Associated with | Chip-card payments | Mobile contactless payments, such as Apple Pay |
| Managed by | Amex, Discover, JCB, Mastercard, UnionPay, Visa | N/A (the article doesn’t say) |
| Shared trait | Encrypted and authenticated, protects against counterfeiting | Same |
| Speed | Noticeably slow, because the chip talks to the processor | Fastest, takes seconds |

**Why businesses should accept NFC**

- **Secure:** tokenization plus biometrics.
- **Fast:** quicker than cash, magstripe and chip.
- **Convenient:** customers increasingly expect to pay with their phones.

To accept it, you need an NFC-enabled reader. Square offers its Reader for contactless and chip, and Tap to Pay on iPhone with Square Point of Sale or Square for Retail. Customers can tap a contactless card or a digital wallet.

**Caveats**

- The piece is marketing content, so the speed and security claims come from Square.
- The article has a few oddities:
    - It says “RDIF” instead of RFID.
    - It says Apple Pay “only works on the most recent iPhone models with Touch ID”. Elsewhere it says iPhone 7 and newer are supported.
    - Android Beam was removed in Android 10, so that tip is out of date.