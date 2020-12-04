import os
import sys
from stringcolor import *
from simple_term_menu import *
from bin.addons.ip_tools import CheckTargetConnection

purple = "\033[38;5;92m"
blue = "\033[38;5;51m"
green = "\033[38;5;47m"
light_blue = "\033[38;5;45m"
reset = "\033[0m"
pink = "\033[38;5;200m"
red = "\033[38;5;196m"
yellow = "\033[38;5;11m"


def menu():
    while True:
        target = input(
            f"{purple}Target{reset}({green}ip{light_blue}:{green}port{light_blue}/{green}url{reset}): "
        )
        if target and not target.isspace():
            if not CheckTargetConnection(target):
                print(f"{red}Error{blue} to connect to the target, try againg{reset}")
            else:
                break

        else:
            print(f"{red}Please, this value cannot be null{reset}")

    attacks = {
        "[0] Ping of Death": "POD",
        "[1] HTTP Flood": "http",
        "[2] Slowloris": "slowloris",
        "[3] Syn Flood": "syn",
        "[4] Icmp Flood": "icmp",
        "[5] Memcached": "memcached",
        "[6] NTP Amplification": "ntp",
        "[7] UDP Flood": "udp",
        "[8] Ssdp Amplification": "ssdp",
        f"[☠] \033[1m{red}ARMAGEDOM{reset} {yellow}(DANGER){reset}": "armagedom",
    }

    title = f"{purple}Method {blue}[Use arrows to move]\033[0m"

    terminal_menu = TerminalMenu(attacks, title=title)
    menu_index = terminal_menu.show()

    for index, attack in enumerate(attacks):
        if index == menu_index:
            method = attacks[attack]
    print(f"{yellow}{method}{green} method selected{reset}")

    while True:
        try:
            threads = input(
                f"{purple}Threads{reset}({green}Enter to default: {light_blue}3{reset}): "
            )
            if threads == "":
                break
            threads = int(threads)
            if threads >= 1 and threads <= 200:
                break
        except ValueError:
            print(f"{red}Please, enter a number between 1 and 200!{reset}")

    while True:
        try:
            time = input(
                f"{purple}Time in seconds{reset}({green}Enter to default: {light_blue}10{pink}s{reset}): "
            )
            if time == "":
                break
            time = int(time)
            if time >= 0:
                break
        except ValueError:
            print(f"{red}Please enter a number greater than 0!{reset}")

    root = True
    for arg in sys.argv:
        if arg == "--no-root":
            root = False

    if threads == "":
        threads = 3

    if time == "":
        time = 10

    return target, method, threads, time, root
