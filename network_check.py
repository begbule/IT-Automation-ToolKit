import socket
import psutil

print("=== Network Adapter Information ===\n")

addrs = psutil.net_if_addrs()

for interface, addr_list in addrs.items():
    print(f"Interface: {interface}")
    for addr in addr_list:
        if addr.family == socket.AF_INET:
            print(f"  IP Address: {addr.address}")
            print(f"  Netmask: {addr.netmask}")
    print()
