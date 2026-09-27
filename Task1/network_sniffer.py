from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime

print("========================================")
print("       CODEALPHA NETWORK SNIFFER")
print("========================================")
print("Starting packet capture...")
print("Capturing for 10 seconds...\n")
packet_number = 0
def packet_callback(packet):
    global packet_number
    try:
        if IP not in packet:
            return
        packet_number += 1
        timestamp = datetime.now().strftime("%H:%M:%S")
        source = packet[IP].src
        destination = packet[IP].dst
        if TCP in packet:
            protocol = "TCP"
            source_port = packet[TCP].sport
            destination_port = packet[TCP].dport
        elif UDP in packet:
            protocol = "UDP"
            source_port = packet[UDP].sport
            destination_port = packet[UDP].dport
        elif ICMP in packet:
            protocol = "ICMP"
            source_port = "-"
            destination_port = "-"
        else:
            protocol = "Other"
            source_port = "-"
            destination_port = "-"
        if Raw in packet:
            payload = bytes(packet[Raw].load)
        else:
            payload = b""
        payload_length = len(payload)
        print(f"[Packet {packet_number}] {timestamp}")
        print(f"Source:        {source}")
        print(f"Destination:   {destination}")
        print(f"Protocol:      {protocol}")
        print(f"Source Port:   {source_port}")
        print(f"Dest Port:     {destination_port}")
        print(f"Payload Length:{payload_length} bytes")
        print(f"Payload:       {payload}")
        print("-" * 45)
    except Exception as error:
        print(f"Error processing packet: {error}")


sniff(
    timeout=10,
    prn=packet_callback,
    store=False
)

print("\n========================================")
print(f"Capture complete. Packets analyzed: {packet_number}")
print("========================================")