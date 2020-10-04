# Import modules
import subprocess
import os
import sys
import socket
import platform
import requests
import ipaddress
from time import sleep
from colorama import Fore
from urllib.parse import urlparse

""" Check if site is under CloudFlare protection """


def __isCloudFlare(link):
    parsed_uri = urlparse(link)
    domain = "{uri.netloc}".format(uri=parsed_uri)
    try:
        origin = socket.gethostbyname(domain)
        iprange = requests.get("https://www.cloudflare.com/ips-v4").text
        ipv4 = [row.rstrip() for row in iprange.splitlines()]
        for i in range(len(ipv4)):
            if ipaddress.ip_address(origin) in ipaddress.ip_network(ipv4[i]):
                print(
                    f"{Fore.RED}[!] {Fore.YELLOW}The site is protected by CloudFlare, attacks may not produce results.{Fore.RESET}"
                )
                sleep(1)
    except socket.gaierror:
        return False


""" Return ip, port """


def __GetAddressInfo(target):
    try:
        ip = target.split(":")[0]
        port = int(target.split(":")[1])
    except IndexError:
        print(
            f"{Fore.RED}[!] {Fore.MAGENTA}You must enter ip and port{Fore.RESET}")
        sys.exit(1)
    else:
        return ip, port


""" Return url (for HTTP method) """


def __GetURLInfo(target):
    if not target.startswith("http"):
        target = f"http://{target}"
    return target


""" Return target """


def GetTargetAddress(target, method):
    methods = [
        "POD",
        "syn",
        "slowloris",
        "http",
        "icmp",
        "memcached",
        "ntp",
        "udp",
        "ssdp"
    ]

    if method in methods and target.startswith("http"):
        parsed_uri = urlparse(target)
        domain = "{uri.netloc}".format(uri=parsed_uri)
        origin = socket.gethostbyname(domain)
        __isCloudFlare(domain)
        return origin, 80
    elif method in methods:
        return __GetAddressInfo(target)
    elif method == "http":
        url = __GetURLInfo(target)
        __isCloudFlare(url)
        return url
    else:
        return target


GetTargetAddress("https://github.com", "POD")

""" Is connected to internet """


def InternetConnectionCheck():
    try:
        requests.get("https://google.com", timeout=4)
    except:
        print(
            f"{Fore.RED}[!] {Fore.MAGENTA}Your device is not connected to the Internet{Fore.RESET}"
        )
        sys.exit(1)


def CheckTargetConnection(target):
    resposta = -1
    if target.startswith("http"):
        target = target.split("//")[1]

    if platform.system().lower() == "windows":
        ping_str = "-n 1"
        resposta = os.system("ping "+ping_str+" "+target+" > NUL")
    else:
        ping_str = "-c 1"
        resposta = os.system("ping "+ping_str+" "+target+" > /dev/null 2>&1")

    return resposta == 0
