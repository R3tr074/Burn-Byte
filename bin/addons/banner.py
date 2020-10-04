from stringcolor import *
dark_blue = "#2F12B3"
blue = "#2D42A3"
pink = "#f535aa"
orange = "#FFAE00"
orange2 = "#FF760D"
orange3 = "#E69D00"
purple = "#7202fc"

space = "  "

pink2 = "\033[38;5;200m"
light_blue = "\033[38;5;51m"
reset = "\033[0m"


def banner():
    print(cs("     )                        )           )       ", pink))
    print(cs("  ( /(    (   (            ( /(  (     ( /(   (   ", orange3))
    print(cs("  )\())  ))\  )(    (      )\()) )\ )  )\()) ))\  ", orange2))
    print(cs(" ((_)\  /((_)(()\   )\ )  ((_)\ (()/( (_))/ /((_) ", orange))
    print(cs(" | |", blue)+cs("(_)(_)", orange)+cs(")(  ((_) _(_/(  ", pink) +
          cs("| |", blue)+cs("(_) )( ) ", pink)+cs("| |_", blue)+cs(" (_))   ", pink))
    print(cs(" | '_ \| || || '_|| ' \)) | '_ \| || ||  _|/ -_)  ", blue))
    print(cs(" |_.__/ \_,_||_|  |_||_|  |_.__/ \_, | \__|\___|  ", dark_blue))
    print(cs("                                 |__/             ", dark_blue))
    print(cs("Ready to burn some servers?                       ", purple))


def main_help():
    banner()
    print(cs("USAGE", purple))
    print(
        f"{space}./burn.py --target <ip:port or url> --method <method or help> [optionals...]")
    print(f"\033[1m{cs('Or this for interactive mode:', purple)}\033[0m")
    print(f"{space}./burn.py cli\n")
    print(cs("FLAGS [OPTIONALS]", purple))
    print(
        f"{space}--threads:\tThreads count (1-200)| default {light_blue}3{reset}")
    print(f"{space}--time:\tTime in seconds| default {light_blue}10{pink2}s{reset}| set {light_blue}0{reset} to infinite time")
    print(f"{space}--banner:\tPrint just the banner")
    print(f"{space}--method:\tSelect the attack method| accepts " +
          cs("help", "#ffcc00")+" flag")
    print(f"\nType: './burn.py -m E-help' to get a reference to learn about each type of attack")


def methods_help():
    banner()
    print(cs("TYPES", purple))
    print(f"{space}POD:      \tPing Of Death involves sending a malformed or otherwise malicious ping")
    print(f"{space}http:     \tHttp flood attack designed to overwhelm a targeted server with HTTP requests")
    print(f"{space}slowloris:\tSlowloris tries to keep many connections to the target web server open")
    print(f"{space}syn:      \tSYN flooding is done by creating connections without closing them")
    print(f'{space}icmp:     \tA ping flood is a simple attack that overwhelms the victim with ICMP "echo request" packets')
    print(f"{space}memcached:\tThe attack spoofs requests to a vulnerable memcached UDP server")
    print(f"{space}ntp:      \tThe NTP amplification attack is a reflection-based volumetric distributed denial of service attack")
    print(f"{space}udp:      \tA flood of UDP is carried out with a large number of requests with the user datagram protocol (UDP)")


def reference():
    methods_help()
    print()
    print(cs("Links to learning", purple))
    print(f"{space}Ping Of Death:")
    print(f"https://www.cloudflare.com/learning/ddos/ping-of-death-ddos-attack")
    print(f"https://www.techopedia.com/definition/4051/ping-of-death")

    print(f"{space}HTTP flood:")
    print(f"https://www.cloudflare.com/learning/ddos/http-flood-ddos-attack")
    print(f"https://www.imperva.com/learn/ddos/http-flood")

    print(f"{space}Slowloris:")
    print("https://www.cloudflare.com/learning/ddos/ddos-attack-tools/slowloris")
    print("https://www.imperva.com/learn/ddos/slowloris")

    print(f"{space}TCP Syn Flood:")
    print("https://www.cloudflare.com/learning/ddos/syn-flood-ddos-attack")
    print("https://www.imperva.com/learn/ddos/syn-flood")

    print(f"{space}Icmp(ping) Flood:")
    print("https://www.cloudflare.com/pt-br/learning/ddos/memcached-ddos-attack")
    print("https://www.imperva.com/learn/ddos/ping-icmp-flood/")

    print(f"{space}Memcached:")
    print("https://www.cloudflare.com/pt-br/learning/ddos/memcached-ddos-attack")

    print(f"{space}NTP Amplification")
    print("https://www.cloudflare.com/learning/ddos/ntp-amplification-ddos-attack")
    print("https://www.imperva.com/learn/ddos/ntp-amplification")

    print(f"{space}UDP flood")
    print("https://www.cloudflare.com/learning/ddos/udp-flood-ddos-attack")
    print("https://www.imperva.com/learn/ddos/udp-flood")


"""
References:
  Ping Of Death:
https://www.cloudflare.com/learning/ddos/ping-of-death-ddos-attack
https://www.techopedia.com/definition/4051/ping-of-death

  HTTP flood:
https://www.cloudflare.com/learning/ddos/http-flood-ddos-attack
https://www.imperva.com/learn/ddos/http-flood

  Slowloris:
https://www.cloudflare.com/learning/ddos/ddos-attack-tools/slowloris
https://www.imperva.com/learn/ddos/slowloris

  TCP Syn Flood:
https://www.cloudflare.com/learning/ddos/syn-flood-ddos-attack
https://www.imperva.com/learn/ddos/syn-flood

  Icmp(ping) Flood:
https://www.cloudflare.com/pt-br/learning/ddos/memcached-ddos-attack
https://www.imperva.com/learn/ddos/ping-icmp-flood/

  Memcached:
https://www.cloudflare.com/pt-br/learning/ddos/memcached-ddos-attack

  NTP Amplification
https://www.cloudflare.com/learning/ddos/ntp-amplification-ddos-attack
https://www.imperva.com/learn/ddos/ntp-amplification

  UDP flood
https://www.cloudflare.com/learning/ddos/udp-flood-ddos-attack
https://www.imperva.com/learn/ddos/udp-flood

"""
