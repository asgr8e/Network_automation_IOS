from netmiko import ConnectHandler
import os
import pandas as pd
import datetime
import csv
import re
import getpass


reader = pd.read_csv("Bandhan_IP.csv")
router_ip = reader["Router_IP"].tolist()
client_id = reader["Client_ID"].tolist()
static_ip = reader["Static_IP"].tolist()

length = len(router_ip)
print("Routers count"+length)
router_ip_set = set(router_ip)
# print((router_ip_set))
for i in range(length):
    for ip in router_ip_set:
        name = ip + ".txt"
        if router_ip[i] == ip:
            with open(name ,"a+") as c:
                c.writelines("ip dhcp pool Distribution-Server 20\n")
                c.writelines(static_ip[i]+"\n")
                c.writelines( client_id[i]+"\n" )

length = len(router_ip_set)
username = input("enter username")
password = getpass.getpass()
for i in range(length):
    cisco1 = {
    "device_type":'cisco_ios' ,
    "host": ip,
    "username": username,
    "password":password ,
    "fast_cli": False,
    "global_delay_factor": 3,
    }
    
    net_connect = ConnectHandler(**cisco1)
    net_connect.enable()
    name = ip + ".txt"
    command=net_connect.send_config_from_file(name)
    net_connect.save_config()
    post_config_devices = [ip[],command[]]
    for i in range(length):
        confirmation=net_connect.send_command('sh run | sec Distribution-Server 20')
        with open ('Final_report.csv',"a+") as report:
            report.writelines(ip[i]+command[i]+"success\n")





