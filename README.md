# Tor IP Rotator (Anonsurf)

A Python script to automatically rotate Tor exit IPs using **Anonsurf** and verify anonymity programmatically.

## Features
- Forces traffic through Tor using Anonsurf
- Rotates Tor exit nodes automatically
- Verifies Tor usage (`IsTor: true`)
- Works inside Kali Linux / WSL Kali

## Requirements
- Kali Linux (bare metal or WSL)
- Tor
- Anonsurf
- iptables (legacy)
- Python 3.8+

## Installation
```bash
sudo apt update
sudo apt install -y tor iptables iproute2 psmisc
pip install -r requirements.txt
