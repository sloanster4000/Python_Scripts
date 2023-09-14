#!/usr/bin/env python3
"""Script authenticate with Palo Alto FW Captive Portal"""
from getpass import getpass
import logging
import requests
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings()

def start_logger():
    """Function for Logging"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)-15s - [%(levelname)-5s] - [%(module)-15.15s] - line_number [%(lineno)3s] - %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )


def captive_portal(user, pswd, site):
    """Function to authenticate with Palo Alto FW Captive Portal"""
    for site in site.split(' '):
        url = f"https://{site}:6082/php/uid.php?vsys=1&rule=0"
        payload = f"escapeUser={user}&user={user}&passwd={pswd}&ok=Login"
        req = requests.post(url, verify=False, data=payload, timeout=10)
        soap = BeautifulSoup(req.text, 'html.parser')
        logging.info('Authenticated with %s', site)
        print(soap.b.string)


if __name__ == '__main__':
    USER = input('username: ')
    PWD = getpass("Enter password for " + USER + " : ")
    SITE = input('Site Code: ')
    try:
        captive_portal(USER, PWD, SITE)
    except requests.exceptions.HTTPError as err:
        logging.error('Http Error Code %s', err)
    except requests.exceptions.RequestException as e:
        logging.error('A connection error occurred: %s', e)
