import os
import sys
from simple_term_menu import *
from rich.console import Console
from bin.addons.banner import banner
from bin.addons.ip_tools import CheckTargetConnection

console = Console()

print = console.print
input = console.input

purple = "blue_violet"
blue = "turquoise2"
green = "green1"
light_blue = "dark_slate_gray2"
pink = "magenta3"
red = "red3"
yellow = "yellow1"


def menu():
    banner()
    while True:
        target = input(
            f"[{purple}]Target([{green}]ip[{light_blue}]:[/{light_blue}]port[/{green}]/[{green}]url[/{green}]):[/{purple}] "
        )
        if target and not target.isspace():
            if not CheckTargetConnection(target):
                print(
                    f"[{red} bold]Error[/{red} bold][{light_blue}] to connect to the target, try againg[/{light_blue}]"
                )
            else:
                break

        else:
            print(f"[{red}]Please, this value cannot be null[/{red}]")

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
        "[☠]  "
        + "\033[38;5;196m"
        + "ARMAGEDDOS "
        + "\033[0m "
        + "\033[38;5;11m"
        + "(DANGER)"
        + "\033[0m": "armageddos",
    }

    title = (
        "\033[38;5;92m"
        + "Method "
        + "\033[38;5;51m"
        + "[Use arrows to move]"
        + "\033[0m"
    )

    terminal_menu = TerminalMenu(attacks, title=title)
    menu_index = terminal_menu.show()

    for index, attack in enumerate(attacks):
        if index == menu_index:
            method = attacks[attack]
    print(f"[{yellow} bold]{method}[/{yellow} bold][{green}] method selected[/{green}]")

    while True:
        try:
            threads = input(
                f"[{purple}]Threads([{green}]Enter to default: [{light_blue}]3[/{light_blue}][/{green}]): "
            )
            if threads == "":
                break
            threads = int(threads)
            if threads >= 1 and threads <= 200:
                break
        except ValueError:
            print(f"[{red}]Please, enter a number between 1 and 200![/{red}]")

    while True:
        try:
            time = input(
                f"[{purple}]Time in seconds([{green}]Enter to default: [{light_blue}]10[/{light_blue}][{pink}]s[/{pink}][/{green}]): [/{purple}]"
            )
            if time == "":
                break
            time = int(time)
            if time >= 0:
                break
        except ValueError:
            print(f"[{red}]Please enter a number greater than 0![/{red}]")

    root = True
    for arg in sys.argv:
        if arg == "--no-root":
            root = False

    if threads == "":
        threads = 3

    if time == "":
        time = 10

    return target, method, threads, time, root
