# Import modules
import os
import sys
import socket
import requests
import ipaddress
from time import sleep
from rich.console import Console
from urllib.parse import urlparse

console = Console()
print = console.print

red = "red3"
yellow = "yellow3"
pink = "magenta3"


def __isCloudFlare(link) -> bool:
    """
    Check if site is under CloudFlare protection
    """
    parsed_uri = urlparse(link)
    domain = "{uri.netloc}".format(uri=parsed_uri)
    try:
        origin = socket.gethostbyname(domain)
        iprange = requests.get("https://www.cloudflare.com/ips-v4").text
        ipv4 = [row.rstrip() for row in iprange.splitlines()]
        for i in range(len(ipv4)):
            if ipaddress.ip_address(origin) in ipaddress.ip_network(ipv4[i]):
                print(
                    f"[{red}][!] [{yellow}]The site is protected by CloudFlare, attacks may not produce results.[/{red}]"
                )
                sleep(1)
    except socket.gaierror:
        return False


def __GetAddressInfo(target: str) -> [str, int]:
    """
    Get ip and port to target
    """
    try:
        ip = target.split(":")[0]
        port = int(target.split(":")[1])
    except IndexError:
        print(f"[{red}][!] [{yellow}]You must enter ip and port[/{red}]")
        sys.exit(1)
    else:
        return ip, port


def __GetURLInfo(target) -> str:
    """
    get url for HTTP method
    """
    if not target.startswith("http"):
        target = f"http://{target}"
    return target


def GetTargetAddress(target: str, method: str) -> str:
    """
    Return target address
    """
    methods = [
        "POD",
        "syn",
        "slowloris",
        "http",
        "icmp",
        "memcached",
        "ntp",
        "udp",
        "ssdp",
        "armageddos",
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


def InternetConnectionCheck() -> bool:
    """
    Test internet connection
    """
    response = -1
    if os.name == "nt":  # if is windows
        response = os.system(f"ping -n 1 google.com > NUL")
    else:
        response = os.system(f"ping -c 1 google.com > /dev/null 2>&1")
    return response == 0


def CheckTargetConnection(target: str) -> bool:
    """
    Test connection to target
    """
    response = -1
    if target.startswith("http"):
        target = target.split("//")[1]
    if target.find(":") != -1:
        target = target.split(":")[0]

    if os.name == "nt":  # if is windows
        response = os.system(f"ping -n 1 {target} > NUL")
    else:
        response = os.system(f"ping -c 1 {target} > /dev/null 2>&1")

    return response == 0
