"""
This script is used to test the availability of a list of servers/hosts by connecting to them through a socket. It uses the socket module in Python.

Disclaimer: This script is for educational purposes only and should be used at your own risk.

Developer: SahanaJayaram, email: sjayaramu@eplus.com
"""

import socket # import socket module to establish the connection
import sys

try:
    # Reserve a port on your computer
    # Refer to default ports
    port = 80 # Port to listen on (non-privileged ports are > 1023)

    # List of Servers/Hosts to test
    hosts_to_test = [
        '127.0.0.1', # Localhost
        'google.com', # Google website
        '127.0.0.2', # Localhost
        '10.1.185.66', # IP address of a server
        '10.1.185.71', # IP address of a server
        '10.1.185.77', # IP address of a server
        '10.1.185.78', # IP address of a server
        '10.1.185.75' # IP address of a server
    ]

    # Iterate the Servers/Hosts list
    for hostname in hosts_to_test:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Get the IP address of the host using gethostbyname()
        host_ip = socket.gethostbyname(hostname)
        print("Socket successfully created to connect Server: " + hostname + " with IP: " + host_ip)

        # Connect to the server using the IP address and port number
        s.connect((host_ip,port))

        # Send some data through the socket to the server
        s.sendall(b'Hello, world')

        # Receive data from the server
        while True:
            data = s.recv(1024)
            if not data:
                break
            s.sendall(data)

        # The server is alive if there is a successful connection
        print("A Server is ALIVE! - " + hostname + " with IP: " + host_ip)
        print("\n")

        # Close the connection
        s.close()

except socket.error:
    # This means that the host could not be resolved
    print("** There was an error resolving the host **", hostname)
    print("A Server looks like DOWN!")
    print("\n")
    sys.exit() # Exit the script

# Note: This script can be further optimized with the use of multithreading to speed up the process of testing multiple servers/hosts.