#!/usr/bin/env python3
# This script is a netcat replacment written in python
# 05/08/2017:   Initial version [ERS]
# 06/05/2017:   Add -v (verbose) to match original NetCat.[ERS]
# 06/05/2017:   Uploaded to github.[ERS]
import socket
import argparse

parser = argparse.ArgumentParser(description='Simple client socket implementation')
parser.add_argument("-v", "--verbose", help="Print Verbose connection", action='store_true')
parser.add_argument('host', help="Host address")
parser.add_argument('port', help="Host port")
args = parser.parse_args()

if args.verbose:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            s.connect((args.host, int(args.port)))
            print("Connected to", s.getpeername())
            s.shutdown(socket.SHUT_WR)
            s.close()
            break
        except OSError as err:
            print(err)
            break
else:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            s.connect((args.host, int(args.port)))
            s.shutdown(socket.SHUT_WR)
            s.close()
            break
        except OSError as err:
            print(err)
            break