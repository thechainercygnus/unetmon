import ipaddress
from os import environ
from time import sleep

from dotenv import load_dotenv

from unetmon import check

load_dotenv()
TARGET_IPS = []
for IP in environ['CHECK_IPS'].split(','):
    TARGET_IPS.append(ipaddress.ip_address(IP))
CHECK_PORT = int(environ['CHECK_PORT'])
CHECK_INTERVAL = int(environ['CHECK_INTERVAL'])

if __name__ == "__main__":
    for TARGET in TARGET_IPS:
        result = check.target_is_up(TARGET, CHECK_PORT)
        print(f"{TARGET} - {result}")
    sleep(CHECK_INTERVAL)
