"""Module providing NETCAT Function"""
#!/usr/bin/env python3
# This script is a netcat replacement written in python
# 05/08/2017:   Initial version [ERS]
# 06/05/2017:   Add -v (verbose) to match original NetCat.[ERS]
# 06/05/2017:   Uploaded to github.[ERS]
# 05/21/2020:   Added socket timeout settings, changed port type as int and removed -v switch. [ERS]
# 05/22/2020:   Added sys exceptions. [ERS]
# 05/28/2020:   Added flag for UDP connections. [ERS]
# 02/27/2025:   Edits added by AI [ERA]
import sys
import socket
import argparse
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Accept arguments from user input
parser = argparse.ArgumentParser(description='Netcat like port checker')
parser.add_argument('host', help="Host address")
parser.add_argument('port', help="Host port", type=int)
parser.add_argument('-u', '--udp', help="Attempt a UDP connection", action='store_true')
args = parser.parse_args()

# Attempt a TCP connection (edited comment)
if not args.udp:  # Changed from 'if args.udp is False:'
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5.5)
        s.connect((args.host, args.port))
        logging.info(f"{args.host} {args.port} TCP port open")
        s.shutdown(socket.SHUT_WR)
        s.close()

    except KeyboardInterrupt:
        logging.info("Script interrupted by user")
        sys.exit()

    except socket.gaierror:
        logging.error('Hostname could not be resolved')
        sys.exit()

    except socket.error:
        logging.error('Could not connect to server')
        sys.exit()

# Attempt a UDP connection (edited comment)
if args.udp:  # Changed from 'if args.udp is True:'
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(5.5)
        s.connect((args.host, args.port))
        logging.info(f"{args.host} {args.port} UDP port open")
        s.shutdown(socket.SHUT_WR)
        s.close()

    except KeyboardInterrupt:
        logging.info("Script interrupted by user")
        sys.exit()

    except socket.gaierror:
        logging.error('Hostname could not be resolved')
        sys.exit()

    except socket.error:
        logging.error('Could not connect to server')
        sys.exit()
