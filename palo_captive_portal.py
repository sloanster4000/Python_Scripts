#!/usr/bin/env python3
import requests
from getpass import getpass
from bs4 import BeautifulSoup
from requests.packages import urllib3
requests.packages.urllib3.disable_warnings()

user = input('username: ')
pw = getpass("Enter password for " + user + " : ")
try:
    url = "https://IPADDRESS:PORT/php/uid.php?vsys=1&rule=0"
    payload = ("escapeUser={}&user={}&passwd={}&ok=Login").format(user, user, pw)
    r = requests.post(url, verify=False, data=payload)
    soap = BeautifulSoup(r.text, 'html.parser')
    print(soap.b.string)
except requests.exceptions.HTTPError as err:
    print('Http Error Code ' + str(err))
except requests.exceptions.RequestException as e:
    print('A connection error occurred: ' + str(e))
