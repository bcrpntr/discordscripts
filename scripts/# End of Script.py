"""
/* Developer: SahanaJayaram, email: sjayaramu@eplus.com */
"""

import csv
import os
import platform

plat = platform.system() # Get the current platform (Windows or Linux)

# Open the CSV file to read the list of hosts/servers/ipaddress
with open('ipaddress-list.csv', 'r') as servers_list:
    servers = csv.DictReader(servers_list)
    # Iterate through each server in the CSV file
    for vm in servers_list:
        print "---- Trying to Ping a Server with IPAddress ----", vm
        
        # Check if the platform is Windows
        if plat == "Windows":
            # Ping the server with 1 packet
            response = os.system("ping -n 1 " + vm)
            pass

        # Check if the platform is Linux
        elif plat == "Linux":
            # Ping the server with 1 packet and a timeout of 3 seconds
            response = os.system("ping -c 1 -W 3 " + vm)
            pass

        # Check the response status code
        if response == 0:
                print "********************************************************************"
                print(vm, 'is UP and reachable!')
                print "********************************************************************"
                print "\n"
        elif response == 2 or 256 or 512: # Check if response code is either 2, 256, or 512
                print "********************************************************************"
                print(vm, 'is DOWN and No response from Server!')
                print "********************************************************************"
                print "\n"
        else:
                print "*********************************************************************"
                print(vm, 'is DOWN and Host Unreachable!')
                print "*********************************************************************"
                print "\n"