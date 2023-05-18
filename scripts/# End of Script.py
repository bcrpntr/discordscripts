"""
Developer: SahanaJayaram, email: sjayaramu@eplus.com
"""

import csv
import os
import platform

plat = platform.system()

# Import the list of hosts/servers/ipaddress from CSV file
with open('ipaddress-list.csv', 'r') as servers_list:
    servers = csv.DictReader(servers_list)
    for vm in servers_list:
        print("---- Trying to Ping a Server with IPAddress ----", vm)
        
        # Check for Windows and Linux Platforms and ping server
        if plat == "Windows":
            response = os.system("ping -n 1 " + vm) # Windows ping command
        elif plat == "Linux":
            response = os.system("ping -c 1 -W 3 " + vm) # Linux ping command

        # Check for response status code and print results
        if response == 0:
            print("********************************************************************")
            print(vm, 'is UP and reachable!')
            print("********************************************************************\n")
        elif response == 2 or 256 or 512:
            print("********************************************************************")
            print(vm, 'is DOWN and No response from Server!')
            print("********************************************************************\n")
        else:
            print("*********************************************************************")
            print(vm, 'is DOWN and Host Unreachable!')
            print("*********************************************************************\n")