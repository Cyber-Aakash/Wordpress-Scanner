import socket 
from colorama import init, Fore
from os import system

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

def is_port_open(host,port):
    s = socket.socket()
    try:
        s.connect((host,port))
        s.settimeout(4)
    except:
        return False
    else:
        return True

def scan_ports(host):
    try:
        for port in range(20,1025):
            if is_port_open(host,port):
                print(f"{GREEN}[+]{host}:{port} is open    {RESET}")
            else:
                print(f"{GRAY}[!]{host}:{port} is closed    {RESET}", end = "\r")
    except KeyboardInterrupt:
        print("\n\n[*]User Requested Interrupt")
        print("[*]Application Stopped")
    