#!/usr/bin/env python3
# This script is a pyshark tool that reads from live interfaces and from saved file.
# 06/16/2020:   Initial version [ERS]
import os
import pyshark
import argparse

#Accept aguments from user input
parser = argparse.ArgumentParser(description='Tcpdump like tool in python using pyshark libary')
parser.add_argument('-f', '--file', help="Read from saved pcap file", action='store')
args = parser.parse_args()

#Read from File
if args.file:
    cap = pyshark.FileCapture(args.file, only_summaries=True)
    for pkt in cap:
        print (pkt)
else:
#Live Capture
    getinterface = os.system("netsh interface show interface")
    print(getinterface)

    print('Choose interface')
    INT = input()

    cap = pyshark.LiveCapture(interface=INT)
    cap.sniff(timeout=5)
    cap

    for pkt in cap:
        print (pkt)