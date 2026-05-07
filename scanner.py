import socket
from datetime import datetime

def port_scan(target, start_port=21, end_port=80):

    try:
        # Resolve hostname to IP address
        target_ip = socket.gethostbyname(target)

        print("-" * 50)
        print(f"Target Host   : {target}")
        print(f"Resolved IP   : {target_ip}")
        print(f"Port Range    : {start_port} - {end_port}")
        print(f"Scan Started  : {datetime.now()}")
        print("-" * 50)

        open_ports = []

        # Scan ports within specified range
        for port in range(start_port, end_port + 1):

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((target_ip, port))

            if result == 0:
                open_ports.append(port)
                print(f"[OPEN] Port {port}")

            sock.close()

        print("-" * 50)

        if open_ports:
            print(f"Scan completed. {len(open_ports)} open port(s) found.")
        else:
            print("Scan completed. No open ports found.")

        print(f"Scan Finished : {datetime.now()}")
        print("-" * 50)

    except socket.gaierror:
        print("[ERROR] Hostname could not be resolved.")

    except socket.error:
        print("[ERROR] Unable to connect to the server.")

    except KeyboardInterrupt:
        print("\n[INFO] Scan interrupted by user.")


target = input("Enter target IP or hostname: ")

port_scan(target)
