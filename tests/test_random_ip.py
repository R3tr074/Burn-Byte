from bin.addons.random_data import random_IP
import re


def test_random_ip():
    ip = random_IP()
    assert re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", ip)
