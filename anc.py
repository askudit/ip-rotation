import subprocess
import time
import requests

i=0

def tor_ip():
    try:
        return requests.get(
            "https://check.torproject.org/api/ip",
            timeout=10
        ).json()
    except:
        return None

subprocess.run(["sudo", "anonsurf", "start"])
time.sleep(8)

while True:
    print(f"\n[+] Rotation {i+1}")
    i+=1
    subprocess.run(["sudo", "anonsurf", "change"])
    time.sleep(10)

    ipinfo = tor_ip()
    print(ipinfo)
