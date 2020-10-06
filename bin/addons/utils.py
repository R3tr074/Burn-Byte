import ctypes
import os
import json
import random
from bin.addons.utils import __path


# Get random IP
def random_IP():
    ip = []
    for _ in range(0, 4):
        ip.append(str(random.randint(1, 255)))
    return ".".join(ip)


# Get random user agent
def random_useragent():
    with open(__path("bin", "config", "user_agents.json"), "r") as agents:
        user_agents = json.load(agents)["agents"]
    return random.choice(user_agents)

# Check root


def root_privileges():
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

# Get universal path


def __path(*args):
    complete_path = args[0]
    if os.name == "nt":
        join = "\\"
    else:
        join = "/"

    for path in args:
        if args[0] == path:
            continue
        complete_path = complete_path+join+path
    return complete_path
