import ctypes
import os
import json
import random


def __path(*args) -> str:
    """
    Get universal path
    """
    complete_path = args[0]
    if os.name == "nt":  # if is windows
        join = "\\"
    else:
        join = "/"

    for path in args:
        if args[0] == path:
            continue
        complete_path = complete_path + join + path
    return complete_path


def random_IP() -> str:
    """
    Get random IP
    """
    ip = []
    for _ in range(0, 4):
        ip.append(str(random.randint(1, 255)))
    return ".".join(ip)


def random_useragent() -> str:
    """
    Get random user agent
    """
    with open(__path("bin", "config", "user_agents.json"), "r") as agents:
        user_agents = json.load(agents)["agents"]
    return random.choice(user_agents)


def root_privileges() -> bool:
    """
    Check root privileges in multiplataform
    """
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin
