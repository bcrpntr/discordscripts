"""
Reserve a port on your computer, iterate through a list of servers/hosts, create a socket, connect with the server, and send and receive data from it. Prints the success or failure of the server connection status.
"""

import socket
import sys

try:
    port = 80 # Port to listen on (non-privileged ports are > 1023)

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

    # Iterate through the list of servers/hosts
    for hostname in hosts_to_test:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host_ip = socket.gethostbyname(hostname)
        print("Socket successfully created to connect Server: " + host_ip)

        # Connect to the server
        s.connect((host_ip,port))

        # Send data to the server
        s.sendall(b'Hello, world')

        # Receive data from the server
        while True:
            data = s.recv(1024)
            if not data:
                break
            s.sendall(data)

        print("A Server is ALIVE! -" ,host_ip)
        print("\n")

except socket.error:
    # This means could not resolve the host
    print("** There was an error resolving the host **", host_ip)
    print("A Server looks like DOWN!")
    print("\n")

    # Close the connection
    s.close()