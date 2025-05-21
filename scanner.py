import socket
import subprocess
from datetime import datetime

target = input("enter the target ip address: ")

def port_scan(target):
    try:
        ip = socket.gethostbyname(target)

        print(f"scanning the target {ip}")
        print("time started: ", datetime.now())

        for port in range(21,80):                #specifying the range
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("Port {}: open".format(port))
            sock.close()
    except socket.gaierror:
        print("hostname could not be resolved.")
    except socket.error:
        print("could not connect to the server.")

port_scan(target)
