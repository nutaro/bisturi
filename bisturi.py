from subprocess import call
from ipaddress import ip_network

ip_range = input("Ip range: ")
nmap_arguments = input("Nmap arguments:").strip().split(' ')
print(nmap_arguments)

hosts = [x for x in ip_network(ip_range).hosts()]

print(hosts)

out_buffer = None
value = call(['nmap'] + nmap_arguments, stdout=out_buffer)

print(out_buffer)
