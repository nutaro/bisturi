import sys

from concurrent.futures import ThreadPoolExecutor, as_completed
from subprocess import call
from ipaddress import ip_network


def orchestrate(range_ip: str, nmap: list) -> None:
    with ThreadPoolExecutor(max_workers=1) as executor:
        hosts = {executor.submit(scan, nmap, str(x)): x for x in ip_network(range_ip).hosts()}
        for executed in as_completed(hosts):
            host = hosts[executed]
            try:
                data = executed.result()
            except Exception as ex:
                print(f'{host} generated an exception: {ex}')
            else:
                print(f'{host} page is {data} bytes')


def scan(nmap: list, ip_address: str) -> None:
    nmap.append(ip_address)
    call(['nmap'] + nmap)


if __name__ == "__main__":
    ip_range = sys.argv[1]
    nmap_args = sys.argv[2:]
    orchestrate(ip_range, nmap_args)
