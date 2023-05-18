"""
Developer: Your Name
Date: Today's Date
Description: Python script to test the connection with a list of servers on a specific port.

"""

import socket # import the socket module to establish connections
import sys # import the sys module to handle errors gracefully

try:
    # Reserve a port on your computer to listen to incoming connections
    """
    Refer for Default Ports: https://geekflare.com/default-port-numbers/
    & http://www.steves-internet-guide.com/tcpip-ports-sockets/
    """
    port = 80 # Port to listen on (non-privileged ports are > 1023)

    # List of servers/hosts to test
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

    # Iterate through the servers/hosts list
    for hostname in hosts_to_test:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Get the IP address of the host/server
        host_ip = socket.gethostbyname(hostname)
        # Print success message after creating a socket object to connect to a server
        print "Socket successfully created to connect Server: " + host_ip

        # Connect to the server using the IP address and port number
        s.connect((host_ip,port))

        # Send some data through the socket
        s.sendall(b'Hello, world')

        # Receive data from the server, keep receiving until there's no more data
        while True:
            data = s.recv(1024)
            if not data:
                break
            # Send the received data back to the server
            s.sendall(data)

        # Print success message indicating the server is alive
        print "A Server is ALIVE! -" ,host_ip
        print "\n"

except socket.error:
    # This means could not resolve the host, print error message and something to indicate server is down
    print "** There was an error resolving the host **", host_ip
    print "A Server looks like DOWN!"
    print "\n"

# Close the socket/connection
s.close()