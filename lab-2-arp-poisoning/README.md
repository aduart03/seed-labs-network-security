# Lab 2 — ARP Poisoning & Man-in-the-Middle Attacks (SEED Labs)

This lab demonstrates ARP cache poisoning and man-in-the-middle (MITM)
techniques using SEED Labs in an isolated virtual environment.

All experiments were performed strictly for educational purposes inside
Docker containers and private networks.

---

## ⚠️ Disclaimer

This lab was conducted ONLY in controlled, isolated environments.

- No real networks were targeted
- No unauthorized systems were accessed
- Do NOT run this code on real networks without permission

---

## Objectives

- Observe normal ARP behavior
- Perform ARP cache poisoning
- Position an attacker as a MITM
- Sniff packets between victim hosts
- Modify packet payloads in transit
- Observe ICMP redirect behavior

---

## Environment

- Platform: SEED Labs
- Execution: Docker containers
- Network: Private subnet (`10.9.0.0/24`)
- Interface: Container-only (`eth0`)
- Tools:
  - Scapy
  - Docker
  - Netcat
  - Linux networking utilities

---

## Contents

### `python_scripts/`
- `arp_poison.py` — Sends spoofed ARP replies to poison victim caches
- `sniff_packet.py` — Passively sniffs IP traffic between hosts
- `modify_packet.py` — Intercepts and modifies TCP packet payloads

### `screenshots/`
Contains screenshots documenting:
- ARP tables before and after poisoning
- Victim and attacker machine setup
- Successful packet interception
- Payload modification and forwarding

Screenshots are grouped by task for clarity.

---

## Key Takeaways

- ARP poisoning enables MITM positioning on local networks
- Packet contents can be intercepted and altered without detection
- These attacks rely on trust assumptions at the network layer
- Proper defenses include encryption, ARP inspection, and network segmentation

