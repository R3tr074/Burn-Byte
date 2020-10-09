from bin.addons.ip_tools import GetTargetAddress
import re


def verify_ip(ip):
    return re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", ip)


def test_get_target_addr_out_method():
    target = "https://google.com"
    method = "outmet"

    assert GetTargetAddress(target, method) == target


def test_get_target_addr_pod():
    https_target = "https://github.com"
    http_target = "http://github.com"
    url_target = "github.com"
    port_target = "80"
    ip_target = "140.82.113.3"

    method = "POD"

    ip, port = GetTargetAddress(https_target, method)
    assert verify_ip(ip) and port == 80

    ip, port = GetTargetAddress(http_target, method)
    assert verify_ip(ip) and port == 80

    url, port = GetTargetAddress(url_target+":"+port_target, method)
    assert url == url_target and port == int(port_target)

    ip, port = GetTargetAddress(ip_target+":"+port_target, method)
    assert verify_ip(ip) and port == int(port_target)


def test_get_target_addr_syn():
    https_target = "https://github.com"
    http_target = "http://github.com"
    url_target = "github.com"
    port_target = "80"
    ip_target = "140.82.113.3"

    method = "syn"

    ip, port = GetTargetAddress(https_target, method)
    assert verify_ip(ip) and port == 80

    ip, port = GetTargetAddress(http_target, method)
    assert verify_ip(ip) and port == 80

    url, port = GetTargetAddress(url_target+":"+port_target, method)
    assert url == url_target and port == int(port_target)

    ip, port = GetTargetAddress(ip_target+":"+port_target, method)
    assert verify_ip(ip) and port == int(port_target)


def test_get_target_addr_slowloris():
    https_target = "https://github.com"
    http_target = "http://github.com"
    url_target = "github.com"
    port_target = "80"
    ip_target = "140.82.113.3"

    method = "slowloris"

    ip, port = GetTargetAddress(https_target, method)
    assert verify_ip(ip) and port == 80

    ip, port = GetTargetAddress(http_target, method)
    assert verify_ip(ip) and port == 80

    url, port = GetTargetAddress(url_target+":"+port_target, method)
    assert url == url_target and port == int(port_target)

    ip, port = GetTargetAddress(ip_target+":"+port_target, method)
    assert verify_ip(ip) and port == int(port_target)


def test_get_target_addr_http():
    https_target = "https://github.com"
    http_target = "http://github.com"
    url_target = "github.com"
    port_target = "80"
    ip_target = "140.82.113.3"

    method = "http"

    ip, port = GetTargetAddress(https_target, method)
    assert verify_ip(ip) and port == 80

    ip, port = GetTargetAddress(http_target, method)
    assert verify_ip(ip) and port == 80

    url, port = GetTargetAddress(url_target+":"+port_target, method)
    assert url == url_target and port == int(port_target)

    ip, port = GetTargetAddress(ip_target+":"+port_target, method)
    assert verify_ip(ip) and port == int(port_target)


def test_get_target_addr_icmp():
    https_target = "https://github.com"
    http_target = "http://github.com"
    url_target = "github.com"
    port_target = "80"
    ip_target = "140.82.113.3"

    method = "icmp"

    ip, port = GetTargetAddress(https_target, method)
    assert verify_ip(ip) and port == 80

    ip, port = GetTargetAddress(http_target, method)
    assert verify_ip(ip) and port == 80

    url, port = GetTargetAddress(url_target+":"+port_target, method)
    assert url == url_target and port == int(port_target)

    ip, port = GetTargetAddress(ip_target+":"+port_target, method)
    assert verify_ip(ip) and port == int(port_target)


def test_get_target_addr_memcached():
    https_target = "https://github.com"
    http_target = "http://github.com"
    url_target = "github.com"
    port_target = "80"
    ip_target = "140.82.113.3"

    method = "memcached"

    ip, port = GetTargetAddress(https_target, method)
    assert verify_ip(ip) and port == 80

    ip, port = GetTargetAddress(http_target, method)
    assert verify_ip(ip) and port == 80

    url, port = GetTargetAddress(url_target+":"+port_target, method)
    assert url == url_target and port == int(port_target)

    ip, port = GetTargetAddress(ip_target+":"+port_target, method)
    assert verify_ip(ip) and port == int(port_target)


def test_get_target_addr_ntp():
    https_target = "https://github.com"
    http_target = "http://github.com"
    url_target = "github.com"
    port_target = "80"
    ip_target = "140.82.113.3"

    method = "ntp"

    ip, port = GetTargetAddress(https_target, method)
    assert verify_ip(ip) and port == 80

    ip, port = GetTargetAddress(http_target, method)
    assert verify_ip(ip) and port == 80

    url, port = GetTargetAddress(url_target+":"+port_target, method)
    assert url == url_target and port == int(port_target)

    ip, port = GetTargetAddress(ip_target+":"+port_target, method)
    assert verify_ip(ip) and port == int(port_target)


def test_get_target_addr_udp():
    https_target = "https://github.com"
    http_target = "http://github.com"
    url_target = "github.com"
    port_target = "80"
    ip_target = "140.82.113.3"

    method = "udp"

    ip, port = GetTargetAddress(https_target, method)
    assert verify_ip(ip) and port == 80

    ip, port = GetTargetAddress(http_target, method)
    assert verify_ip(ip) and port == 80

    url, port = GetTargetAddress(url_target+":"+port_target, method)
    assert url == url_target and port == int(port_target)

    ip, port = GetTargetAddress(ip_target+":"+port_target, method)
    assert verify_ip(ip) and port == int(port_target)


def test_get_target_addr_udp():
    https_target = "https://github.com"
    http_target = "http://github.com"
    url_target = "github.com"
    port_target = "80"
    ip_target = "140.82.113.3"

    method = "ssdp"

    ip, port = GetTargetAddress(https_target, method)
    assert verify_ip(ip) and port == 80

    ip, port = GetTargetAddress(http_target, method)
    assert verify_ip(ip) and port == 80

    url, port = GetTargetAddress(url_target+":"+port_target, method)
    assert url == url_target and port == int(port_target)

    ip, port = GetTargetAddress(ip_target+":"+port_target, method)
    assert verify_ip(ip) and port == int(port_target)


def test_get_target_addr_armagedom():
    https_target = "https://github.com"
    http_target = "http://github.com"
    url_target = "github.com"
    port_target = "80"
    ip_target = "140.82.113.3"

    method = "armagedom"

    ip, port = GetTargetAddress(https_target, method)
    assert verify_ip(ip) and port == 80

    ip, port = GetTargetAddress(http_target, method)
    assert verify_ip(ip) and port == 80

    url, port = GetTargetAddress(url_target+":"+port_target, method)
    assert url == url_target and port == int(port_target)

    ip, port = GetTargetAddress(ip_target+":"+port_target, method)
    assert verify_ip(ip) and port == int(port_target)
