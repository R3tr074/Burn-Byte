from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# Define styled print
print = Console().print

# Define colors
orange = "orange1"
pink = "magenta3"
blue2 = "dodger_blue2"
blue3 = "blue3"
yellow = "yellow1"
red = "red3"
light_blue = "dark_slate_gray2"
green = "green1"


def banner() -> None:
    """
    print Burn Byte banner
    """
    print("    )                        )           )       ", style=pink)
    print(" ( /(    (   (            ( /(  (     ( /(   (   ", style=orange)
    print(
        f" )\())  [{pink}]))\  )([/{pink}]    (      )\()) )\ )  )\()) ))\  ",
        style=orange,
    )
    print(
        f"((_[{pink}])\  /((_)[/{pink}](()\   )\ )  ((_)\ (([{pink}])/( (_))/ /[/{pink}]((_) ",
        style=orange,
    )
    print(
        "| |"
        + f"[{orange}] (_)(_)[/{orange}]"
        + f"[{pink}])( ((_) _(_/([/{pink}]  "
        + f"| |[{pink}] (_) )( )  [/{pink}]"
        + f"| |[{pink}]_  (_))[/{pink}]",
        style=blue2,
    )
    print(
        f"[{blue2}]"
        + "| '_ \| || || '_|| ' \)) | '_ \| || ||  _|/ -_)  "
        + f"[/{blue2}]",
        style=blue2,
    )
    print("|_.__/ \_,_||_|  |_||_|  |_.__/ \_, | \__|\___|  ", style=blue3)
    print("                                |__/             ", style=blue3)
    print("Ready to burn some servers?                      ", style=red)
    print()


def main_help() -> None:
    """
    print global help message
    """
    banner()
    usage_complete = Panel(
        f"[{red}]./burn.py [/{red}]"
        + f"[{light_blue}]--target [/{light_blue}]"
        + f"[{pink}]<ip:port or url> [/{pink}]"
        + f"[{light_blue}]--method [/{light_blue}]"
        + f"[{pink}]<method or help> [/{pink}]"
        + f"[{green}]optionals...[/{green}]",
        expand=True,
        width=78,
    )
    usage_interactive = Panel(
        f"[{red}]./burn.py [/{red}]" + f"[{pink}]-i[/{pink}]",
        expand=True,
        width=17,
    )

    print(f"[{green}]Usage:[/{green}]")
    print(usage_complete)
    print(f"[{green}]Or this for interactive mode:[/{green}]")
    print(usage_interactive)

    table = Table(title="FLAGS", show_lines=False)
    table.add_column("flag", justify="right", style="cyan", no_wrap=True)
    table.add_column("what does", style="magenta")
    table.add_column("default", justify="right")
    table.add_column("required", justify="right")
    table.add_column("help", justify="right", style="green", no_wrap=True)

    table.add_row("--threads", "Threads count (1-200)", "3 threads", "No")
    table.add_row(
        "--time",
        "Time in seconds",
        "3 seconds",
        "No",
        f"set [{light_blue}]0[/{light_blue}] to infinite time",
    )
    table.add_row("--banner", "Print just the banner", "", "No")
    table.add_row(
        "--method",
        "Select the attack method",
        "",
        "Yes",
        f'accepts [{light_blue}]help[/{light_blue}] flag, "-m E-help"',
    )
    table.add_row(
        "--target",
        "Select the target",
        "",
        "Yes",
        f"https://web.com|web.com:80|127.0.0.1:22",
    )

    print(table)


def methods_help() -> None:
    """
    print methods help message
    """
    banner()
    table = Table(title="Attacks", show_lines=True)
    table.add_column("Attack type", justify="right", style="cyan", no_wrap=True)
    table.add_column("Description", style="green3")

    table.add_row(
        "POD", "Ping Of Death involves sending a malformed or otherwise malicious ping"
    )
    table.add_row(
        "http",
        "Http flood attack designed to overwhelm a targeted server with HTTP requests",
    )
    table.add_row(
        "slowloris",
        "Slowloris tries to keep many connections to the target web server open",
    )
    table.add_row(
        "syn",
        "SYN flooding is done by creating connections without closing them",
    )
    table.add_row(
        "icmp",
        'A ping flood is a simple attack that overwhelms the victim with ICMP "echo request" packets',
    )
    table.add_row(
        "memcached",
        "The attack spoofs requests to a vulnerable memcached UDP server",
    )
    table.add_row(
        "ntp",
        "The NTP amplification attack is a reflection-based volumetric distributed denial of service attack",
    )
    table.add_row(
        "udp",
        "A flood of UDP is carried out with a large number of requests with the user datagram protocol (UDP)",
    )
    table.add_row(
        "ssdp",
        "SSDP enabled network devices that are also accessible to UPnP from the internet are an easy source for generating SSDP amplification floods.",
    )
    table.add_row(
        f"[{yellow}]☢ [{red}]ARMAGEDDOS[/{red}] ☢[/{yellow}]",
        f"[bold]Armageddos uses all methods together in an attack.[/bold]",
    )
    print(table)


def reference() -> None:
    """
    print reference and indications
    """
    methods_help()
    print()
    print(f"[{blue2}]Links to learning[/{blue2}]")
    print("Burn Byte documentation:")
    print("https://www.burn-byte.tk")


"""
References:
  https://www.burn-byte.tk
"""
