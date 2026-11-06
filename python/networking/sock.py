import socket

host = "www.google.com"

try:
    ip = socket.gethostbyname(host)
    print(f"IP address of {host} is {ip}")
except socket.gaierror:
    print(f"Could not resolve {host}")
    