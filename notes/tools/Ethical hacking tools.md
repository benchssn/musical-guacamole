## Top Ethical Hacking Tools 2026: Notes

**Core idea:** Ethical and malicious hacking use the same tools. What separates them is intent and authorisation. Tools are used to find weaknesses before attackers do, validate vulnerabilities, and support compliance.

### Choosing tools: by target

- **Web apps:** Burp Suite, OWASP ZAP, Nikto, SQLmap
- **Networks:** Nmap, Wireshark, Angry IP Scanner
- **Wireless:** Aircrack-ng, Kismet, Wifite
- **Active Directory / Windows:** BloodHound, Impacket, CrackMapExec
- **Cloud:** Prowler, ScoutSuite, Pacu
- **Passwords:** Hashcat, John the Ripper, Hydra
- **OSINT / recon:** Maltego, theHarvester, Shodan
- **Full pentests:** Kali Linux (300+ tools bundled), Parrot OS

### Choosing tools: by level

- **Beginner:** Start with Kali Linux.
- **Intermediate:** Get comfortable with Metasploit, Burp Suite Pro and Nmap scripting, then move into scripting.
- **Advanced:** Combine frameworks, write custom Nuclei templates, and use C2 frameworks.

### Tools by category (47 in total)

**Recon and OSINT**

- **Nmap:** Port scanning and service/OS detection. Beginner to advanced. SYN scans need root, and aggressive scans can trip IDS/IPS.
- **Shodan:** Finds exposed servers, IoT devices and databases. Free tier, $49/yr membership, $899/yr API.
- **Maltego:** Relationship mapping. Free community edition, Pro $999/yr.
- **Amass:** Attack surface discovery and subdomain enumeration.
- **theHarvester:** Collects emails, subdomains and IPs from public sources.

**Network analysis**

- **Wireshark:** Live packet analysis.
- **Netcat:** Port communication, banner grabbing.
- **Masscan:** Very fast internet-scale port scanning.
- **CrackMapExec:** AD testing and lateral movement simulation.

**Web app**

- **Burp Suite:** The standard for interception and testing. Community is free, Pro is about $449/yr.
- **OWASP ZAP:** Free automated scanning.
- **SQLmap:** SQL injection automation.
- **Nuclei:** Template-based scanning, popular for automation.
- **ffuf:** Fuzzing for hidden directories and endpoints.
- **Nikto:** Web server scanner, checks 6,700+ risky files.

**Wireless**

- **Aircrack-ng:** WPA/WPA2 auditing.
- **Kismet:** Passive detection.
- **Wifite:** Automated Wi-Fi auditing.
- **Bettercap:** Interception and monitoring framework.

**Passwords**

- **Hashcat:** GPU-accelerated cracking. Without a GPU, strong hashes like bcrypt are impractical.
- **John the Ripper:** Classic auditor with auto hash detection.
- **Hydra:** Online brute force. It is noisy and can lock accounts, so check scope first.
- **Mimikatz:** Windows credential extraction.

**Exploitation and red team**

- **Metasploit:** Community is free, Pro is $499/yr. Default Meterpreter payloads are caught by modern EDR.
- **Cobalt Strike:** Adversary simulation and C2, about $5,900/operator/yr.
- **BloodHound:** Maps AD privilege escalation paths.
- **Sliver:** Open-source C2.
- **Impacket:** Python protocol toolkit, used for Kerberoasting among other things.

**Cloud**

- **ScoutSuite:** Multi-cloud auditing.
- **Prowler:** AWS auditing and compliance.
- **Trivy:** Container and image scanning.
- **kube-hunter:** Kubernetes weaknesses.
- **Checkov:** Infrastructure-as-code misconfiguration scanning.

**API**

- **Postman:** Endpoint and auth testing.
- **Kiterunner:** Hidden endpoint discovery.
- **SoapUI:** REST and SOAP testing.
- **mitmproxy:** Intercepting proxy.

**AI-assisted**

- ShellGPT, PentestGPT, ChatGPT, Claude and Microsoft Copilot are listed for scripting, automation, research and documentation.

**Forensics and malware**

- **Ghidra:** Reverse engineering.
- **Volatility:** Memory forensics.
- **Autopsy:** Disk analysis.
- **YARA:** Malware classification rules.

### Mobile

- **Termux:** Linux terminal on Android.
- **Drozer:** Full Android app assessment framework, described as the most complete.
- **Frida:** Dynamic instrumentation for iOS and Android.
- **cSploit and NetCut:** Need root.
- Also listed: Fing and WPS WPA Tester.
- Only use these on devices and networks you own or are authorised to test.

### Operating systems

- **Kali:** The default, with the widest tool coverage.
- **Parrot OS:** Lightweight and privacy-focused.
- **BlackArch:** Arch-based, 2,800+ tools, for advanced users.
- **REMnux:** Malware analysis and reverse engineering.

### Hardware

- **Wireless adapter:** Needs monitor mode and packet injection (Alfa AWUS036ACH or NHA). This matters more than the laptop.
- **Other kit:** Rubber Ducky or Flipper Zero, Raspberry Pi 5 as a drop box, bootable Kali USB, LAN tap, RTL-SDR.

### Free toolkit by phase

- **Recon:** Nmap, theHarvester, Recon-ng
- **Vulnerability scanning:** OpenVAS, Nuclei, Nikto
- **Exploitation:** Metasploit Community, SQLmap
- **Web:** Burp Community, ZAP
- **Passwords:** Hashcat, John, Hydra
- **Wireless:** Aircrack-ng, Wifite, Kismet
- **AD:** BloodHound, Impacket, CME
- **Forensics:** Wireshark, Volatility
- **C2:** Sliver
- **Reporting:** Dradis Community, Ghostwriter

### Wi-Fi cracking

- **How it works:** WPA2-PSK cracking captures the 4-way handshake, then runs an offline dictionary or brute-force attack. Because the cracking is offline, it can’t be detected in real time.
- **Crack times (RTX 4090):**
    - 8 lowercase characters: under 1 minute
    - 8 alphanumeric: about 22 minutes
    - 10 alphanumeric: about 3 days
    - 12 mixed with symbols: centuries
    - WPS 8-digit PIN: about 4 hours using Reaver
- **Defences:**
    - Disable WPS.
    - Use WPA3 where supported.
    - Enforce 16+ character passphrases.

### Takeaways

1. Match tools to the target and your skill level. Don’t install everything.
2. Nmap, Burp, Wireshark and Metasploit are the core four to learn first.
3. Cloud, API and AD skills are increasingly in demand.
4. Always work within written scope. Brute-force and scanning tools generate logs and can lock accounts.
5. Everything needed to start is free.