import sys

from subprocess import call
from ipaddress import ip_network


def scan(range_ip: str, nmap: list) -> None:
    hosts = [x for x in ip_network(range_ip).hosts()]
    out_buffer = None
    call(['nmap'] + nmap, stdout=out_buffer)


if __name__ == "__main__":
    ip_range = sys.argv[1]
    nmap_args = sys.argv[2:]
    scan(ip_range, nmap_args)
