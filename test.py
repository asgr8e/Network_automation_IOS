from netmiko import ConnectHandler
import os
import pandas as pd
import datetime
import csv
import re
import getpass

ip='10.18.88.254'
username = input("enter username")
password = getpass.getpass()
cisco1 = {
    "device_type":'cisco_ios' ,
    "host": ip,
    "username": username,
    "password":password ,
    "fast_cli": False,
    "global_delay_factor": 3,
    }
with open ('report.csv',"w+") as f:
    f.writelines("")
    f.close()
net_connect = ConnectHandler(**cisco1)
net_connect.enable()
command=net_connect.send_command("sh ip int brie")
print(command)