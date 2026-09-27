# CodeAlpha Network Sniffer

## Project Overview

This project is a basic network packet sniffer developed in Python as part of the CodeAlpha Cyber Security Internship.

The program captures network packets and analyzes important information such as source IP address, destination IP address, network protocol, source and destination ports, and packet payload.

The project was developed using the Scapy library.

## Features

- Captures network packets
- Displays packet number
- Displays timestamp
- Identifies source IP address
- Identifies destination IP address
- Identifies network protocol
- Displays source and destination ports
- Extracts packet payload
- Displays payload length
- Handles packet-processing errors
- Displays a final packet count after capture

## Technologies Used

- Python
- Scapy
- Npcap
- Visual Studio Code
- Windows

## Protocols Detected

The sniffer identifies:

- TCP
- UDP
- ICMP
- Other IP-based traffic

## How It Works

The program uses Scapy to capture packets from the network interface.

For every captured IP packet, the program extracts:

1. Source IP address
2. Destination IP address
3. Protocol
4. Source port
5. Destination port
6. Payload
7. Payload length
8. Timestamp

The program captures traffic for 10 seconds and then displays the total number of packets analyzed.

## Installation

Install Scapy using:

    py -m pip install scapy

Npcap is also required on Windows for packet capture.

## How to Run

Open the terminal in the project directory:

    cd "$HOME\Desktop\CodeAlpha_NetworkSniffer"

Run the program:

    py network_sniffer.py

The program will capture packets for 10 seconds and display the analyzed information.

## Sample Output

    ========================================
           CODEALPHA NETWORK SNIFFER
    ========================================
    Starting packet capture...
    Capturing for 10 seconds...

    [Packet 1] 13:24:57
    Source:        192.168.0.100
    Destination:   192.168.0.1
    Protocol:      UDP
    Source Port:   2031
    Dest Port:     53
    Payload Length: XX bytes
    Payload:       b'...'
    ---------------------------------------------

    Capture complete. Packets analyzed: XXXX

## Learning Outcomes

Through this project, I learned:

- Basics of network packet structure
- Source and destination addressing
- TCP, UDP and ICMP protocols
- Network ports
- Packet payloads
- Basic packet analysis using Scapy
- Practical network traffic monitoring

## Internship Task

This project was completed as part of:

**CodeAlpha Cyber Security Internship — Task 1: Basic Network Sniffer**

The task focuses on capturing and analyzing network traffic using Python and Scapy.