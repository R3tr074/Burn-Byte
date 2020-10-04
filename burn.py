#!/bin/python3
import os
import sys
from bin.crash import CriticalError

# Go to the current directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Define colors
red = "\033[38;5;196m"
blue = "\033[38;5;51m"
yellow = "\033[38;5;11m"
reset = "\033[0m"

# Import modules
try:
    import bin.addons.clean
    from bin.method import AttackMethod
    from bin.addons.banner import main_help
    from bin.addons.utils import root_privileges
    from bin.addons.arg_manager import arg_manager
except ImportError as err:
    CriticalError("Failed import some modules", err)
    sys.exit(1)

# Parse args
args = arg_manager(sys.argv)

if type(args) is int:
    if args != 0:
        sys.exit(1)
    else:
        sys.exit(0)

threads = args["threads"]
time = int(args["time"])
target = args["target"]
method = args["method"]
root = args["root"]

if not root_privileges() and root:
    print(
        f"{red}Error:{blue} superuser privileges are required to use correctly{reset}")
    print(
        f"{yellow}If you want to ignore this error, use the {red}--no-root{yellow} flag. (Not recommended){reset}")
    sys.exit(1)


if __name__ == "__main__":
    with AttackMethod(
        duration=time, name=method, threads=threads, target=target
    ) as Flood:
        Flood.Start()
