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
