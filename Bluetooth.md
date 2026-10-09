# Bluetooth

**The short version:** Bluetooth is a low-power, short-range radio technology that lets devices talk to each other directly, with no router in between. The Bluetooth Special Interest Group (SIG) sets the standards manufacturers build to. The article was written around 2020.

### The two types of Bluetooth

|  | Bluetooth Classic (BR/EDR) | Bluetooth Low Energy (LE) |
| --- | --- | --- |
| Popularity | Less common | By far the more popular |
| Data rate | About 3 Mbps | 1 or 2 Mbps |
| Power use | Higher | Much lower |
| Topology | Point-to-point only (two devices) | Point-to-point, broadcast, or mesh |
| Pairing | Always required | Optional, depending on the product |
| How devices connect | Automatic “conversation” when in range | One device advertises, another scans for it |

Both types use the same radio band, 2.400 to 2.4835 GHz. This is an ISM band (industrial, scientific, medical) that baby monitors, garage-door openers and cordless phones also use. Avoiding interference between them is essential.

### How it operates

- **Classic:** Paired devices automatically check whether they trust each other and have data to share, then form a network. The user usually doesn’t need to do anything.
- **LE:** A device that wants to be found sends out small advertising packets. Another device scans for them, often when the user taps a button in an app. The user then picks a device from the list to connect to.
- **Piconets:** Peripherals connected to the same central device, such as a watch and a fitness tracker on one phone, form a personal-area network. The network can span a building or just the distance from your pocket to your wrist.
- **Adaptive frequency hopping:** Members of a piconet hop between radio channels together. They learn which channels have interference and avoid them. This is why Bluetooth works well where many wireless devices are crowded together.

### Range

The article says Bluetooth can reach over 1 km (3,280 ft), though many products, such as headphones, are set up for very short range. Manufacturers tune the range to balance distance, battery life and signal quality.

| Factor | What it means |
| --- | --- |
| Radio spectrum | The frequency band suits wireless communication |
| Physical layer (PHY) | Sets data rate, error detection and correction, and interference protection |
| Receiver sensitivity | The weakest signal a receiver can still decode correctly |
| Transmission power | More power gives more range but drains the battery faster |
| Antenna gain | How well electrical signals are converted to radio waves and back |
| Path loss | Distance, humidity, and materials like wood, concrete or metal weaken the signal |

A recent update added **forward error correction (FEC)**. It corrects errors at the receiving end and improves effective range by four times or more without extra transmission power.

### Security

- **Pairing:** Exchanges security keys so the two devices trust each other. A device that requires pairing won’t connect to an unpaired one.
- **Encryption:** Data between devices can be encrypted so other devices can’t read it.
- **Address disguising:** A device’s identifying address can be changed every few minutes, which prevents tracking.
- **Authentication codes:** Some devices need a code during pairing. In the car example, you type in a number shown on the car’s display to confirm the pairing is authorized. After that you don’t need to pair again.
- **Visibility control:** You can set a device to “nondiscoverable” or turn Bluetooth off.
- **Multiple connections:** A computer can handle many Bluetooth connections at once. Accessories such as keyboards and headphones usually connect to one device at a time. Some can be paired with several devices but connect to only one at once.

The article says Bluetooth’s security can meet strict standards such as FIPS.

### Trivia and FAQ highlights

- **The name:** It comes from Harald Bluetooth, a Danish king from the late 900s who united Denmark and part of Norway. The name nods to the Nordic companies’ importance in communications.
- **Wi-Fi vs Bluetooth:** Wi-Fi mainly connects devices to the internet. Bluetooth transfers data between devices over short distances.
- **Latest version (at time of writing):** Bluetooth 5.2, plus LE Audio announced in January 2020.
- **Adding Bluetooth to a PC:** Most PCs already have it. If yours doesn’t, plug in a USB adapter and install the manufacturer’s drivers.