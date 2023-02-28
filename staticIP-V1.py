from netmiko import ConnectHandler
import os
import datetime
import csv
import re
import getpass

router_ip=[]
client_id=[]
static_ip=[]


with open ("Bandhan_IP.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        router_ip.append(row['Router_IP'])
        client_id.append(row['Client_ID'])
        static_ip.append(row['Static_IP'])
    for i in range(len(router_ip)):
        for ip in router_ip:
            print(ip)
            name=(ip + ".txt")
            if router_ip[i]==ip:
                with open (name,'a+') as c:
                    c.writelines(static_ip[i]+'\n')
                    c.writelines(client_id[i]+'\n')


for ip in router_ip:
    cisco1 = {
        "device_type":'cisco_ios' ,
        "host": ip,
        "username": 'cisco',
        "password":'cisco' ,
        "fast_cli": False,
        "global_delay_factor": 3,
        }
        
    net_connect = ConnectHandler(**cisco1)
    net_connect.enable()
    name = ip + ".txt"
    command=net_connect.send_config_from_file(name)
    print(command)
    net_connect.save_config()
    confirmation=net_connect.send_command('sh run | sec Distribution-Server20')
    #finding version in output using regular expressions
    pattern=("ip dhcp pool Distribution-Server 20")
    match = re.search(pattern,confirmation)
    if match:
        with open ('Final_report.txt',"a+") as f:
            f.writelines(ip+ " " +pattern+" success")
            f.writelines("\n")
            f.close()
                            
    else:
        with open ('Final_report.txt',"a+") as f:
            f.writelines(ip+ " " +pattern+" failed")
            f.writelines("\n")
            f.close()


            
    