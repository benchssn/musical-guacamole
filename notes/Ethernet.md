# Ethernet

**The short version**

Ethernet is the standard way to connect devices to a network with a physical cable. It is a set of rules that tells devices how to package and send data so other devices on the same network can understand it. The cable itself is just the wire the data travels along.

**Why people still use it**

Offices, schools, hospitals and gamers use Ethernet because it is fast, reliable and hard for outsiders to break into. It beat early rivals like IBM’s token ring because it was cheap, and it stayed popular because each new version still works with older equipment. Speeds have gone from 10 Mbps originally to as much as 400 Gbps today.

**Pros and cons**

| Good | Not so good |
| --- | --- |
| Low cost | Best for small, short-distance networks |
| Fast and reliable | You’re tied to a cable, so you can’t move around |
| Secure (you have to plug in) | Very long cables can cause interference |
| Works with older equipment | Slows down when traffic is heavy |
| Resists interference | Poor for real-time or interactive uses |
|  | Hard to trace which cable or device is causing a fault |

**Ethernet vs. Wi-Fi**

|  | Ethernet | Wi-Fi |
| --- | --- | --- |
| Connection | Cable | Wireless signal |
| Speed | Faster and steadier | Varies with interference |
| Delay (latency) | Lower | Higher |
| Security | Stronger by default | Needs encryption |
| Mobility | Limited | Connect from anywhere |
| Setup | More work | Easier |

**How it works**

- Ethernet works at the bottom two layers of the standard network model: the physical layer (cables and signals) and the data link layer (addressing and error checking).
- Data is sent in **frames**. Each frame holds the data itself, the sender’s and receiver’s hardware addresses, optional VLAN and priority tags, and error-checking information. Each frame is wrapped in a **packet** that marks where it starts.
- Early Ethernet used coaxial cable and **hubs**. A hub copies everything to every connected device, so devices could collide if they sent at the same time. A rule called CSMA/CD fixed this by making devices check that the line was free before sending.
- Most networks now use **switches** instead. A switch sends data only to the device it is meant for, which is faster and more secure.
- Today’s cables are usually twisted-pair copper or fiber optic. Every computer needs a network interface card (NIC) to connect.

**Common cable types**

- **Cat5** supports regular and 100 Mbps Ethernet.
- **Cat5e** handles Gigabit Ethernet (1,000 Mbps).
- **Cat6** handles 10 Gigabit Ethernet.
- **Crossover cables** connect two similar devices directly, with no switch or router in between.

**Milestones**

Xerox engineers developed Ethernet in the 1970s, and the first official standard was approved in 1983. Fast Ethernet (100 Mbps) arrived in the 1990s. Later additions include VLAN tagging (802.3ac) and Power over Ethernet (802.3af), which sends power and data down the same cable.

One correction to the article: it lists the 802.11 standards (a/b/g/n/ac/ax) in its Ethernet timeline. Those are Wi-Fi standards, not Ethernet ones.