"""
Developer: SahanaJayaram, email: sjayaramu@eplus.com
"""

import socket # Import socket library for creating socket objects
import sys

try:
  # Reserve a port on your computer.
  # Get the Connect() system call to connect to eg:- port 80 for HTTP, port 443 for HTTPS etc.
  port = 80 # Port to listen on (non-privileged ports are > 1023)
  
  # List of Servers/Hosts that needed to be tested.
  hosts_to_test = ['127.0.0.1',
                   'google.com',
                   '127.0.0.2',
                   '10.1.185.66',
                   '10.1.185.71',
                   '10.1.185.77',
                   '10.1.185.78',
                   '10.1.185.75'
                  ]
  
  # Iterate the Servers/Hosts list.
  for hostname in hosts_to_test:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object with IP version 4 and TCP.
      host_ip = socket.gethostbyname(hostname) # Resolve the IP address of the hostname.
      print "Socket successfully created to connect Server: " + host_ip

      # Connect to the server.
      s.connect((host_ip, port))
      
      # Send some data through a socket.
      s.sendall(b'Hello, world')

      # Receive data from the server
      while True:
          data = s.recv(1024)
          if not data:
              break
          s.sendall(data)

      print "A Server is ALIVE! -" ,host_ip
      print "\n"

      s.close() # Close the connection.

except socket.error:
  # Error handling when the host is unresolvable.
  print "** There was an error resolving the host **", host_ip
  print "A Server looks like DOWN!"
  print "\n"
  # sys.exit() # Uncomment this statement to exit the execution when an error has been returned.