#!/usr/bin/env python3
# This script is a simple IP calculator
# 10/13/2016:       Initial version [ERS]
# 5/9/2017:         Add argparse module for command line flags.
# 11/16/2020:       Remove argparse remove IPAddress module
import ipaddress

IADD = input("IP: " )
MASK = input("Subnet: ")

host = ipaddress.IPv4Address(IADD)
net = ipaddress.IPv4Network(IADD + '/' + MASK, False)
print('IP:', IADD)
print('Mask:', MASK)
print('Subnet:', ipaddress.IPv4Address(int(host) & int(net.netmask)))
print('Host:', ipaddress.IPv4Address(int(host) & int(net.hostmask)))
print('Broadcast:', net.broadcast_address)
for address in net:
    print('Range:', address)
