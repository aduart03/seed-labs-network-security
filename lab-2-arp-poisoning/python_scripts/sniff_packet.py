from scapy.all import *

def pkt_callback(pkt):
    if IP in pkt:
        print(f"[+] Intercepted packet: {pkt[IP].src} -> {pkt[IP].dst}")
        pkt.show()

print("[*] Sniffing traffic between A and B...")
sniff(filter="ip", iface="eth0", prn=pkt_callback)
