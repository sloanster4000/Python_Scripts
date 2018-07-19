#!/usr/bin/env python3
# This script is a simple IP calculator
# 10/13/2016:      Initial version
# 5/9/2017:        Add argparse module for command line flags.
#Copyright (c) 2018 Sloanster4000
#Licensed under the terms of LICENSE included in this project

from netaddr import IPAddress, IPNetwork, IPRange
from argparse import ArgumentParser

def parse_cl():
    parser = ArgumentParser(description='Simple IP Calculator')
    parser.add_argument('-i', '--ip', required=True, help='IP address')
    parser.add_argument('-s', '--sub', required=True, help='SubnetMask')
    return parser.parse_args()

def calc(ip, sub):
    sub = IPAddress(sub).netmask_bits()
    net = ('{}/{}'.format(ip, sub))
    ip = IPNetwork(net)
    print('Ip', ip)
    print('SubnetID', ip.network)
    print('Broadcast', ip.broadcast)
    print('Range', ip.network +1, ip.broadcast -1)

if __name__ == '__main__':
    args = parse_cl()
    calc(args.ip, args.sub)
