"""
This script checks the connectivity of a list of servers/hosts to the specified port.
If successful, it prints "A Server is ALIVE! - {IP}", and if unsuccessful, it prints "A Server looks like DOWN!".
"""

import socket
import sys

try:
    # Port to listen on (non-privileged ports are > 1023)
    port = 80

    # List of Servers/Hosts
    hosts_to_test = [
        '127.0.0.1',
        'google.com',
        '127.0.0.2',
        '10.1.185.66',
        '10.1.185.71',
        '10.1.185.77',
        '10.1.185.78',
        '10.1.185.75'
    ]

    # Iterates through each server/host in the list
    for hostname in hosts_to_test:
        # Create a TCP/IP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Gets the IP address of the host
        host_ip = socket.gethostbyname(hostname)
        print("Socket successfully created to connect to Server: " + host_ip)

        # Connects to the server
        s.connect((host_ip, port))

        # Sends some data through the socket
        s.sendall(b'Hello, world')

        # Waits to receive data
        while True:
            data = s.recv(1024)
            if not data:
                break
            s.sendall(data)

        # If the socket has made a successful connection, print the message
        print("A Server is ALIVE! -", host_ip)
        print("\n")

except socket.error:
    # If an error occurs, print the error message and print that the server is down
    print("** There was an error resolving the host **", host_ip)
    print("A Server looks like DOWN!")
    print("\n")

finally:
    # Close the connection
    s.close()