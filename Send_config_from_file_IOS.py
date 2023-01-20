import getpass

from netmiko import ConnectHandler
cisco_device = {
       'device_type': 'cisco_ios',
       'host': '10.75.245.94',
       'username': 'cisco',
       'password': 'cisco',
       'port': 22,             # optional, default 22
       'secret': 'cisco',      # this is the enable password
       'verbose': False         # optional, default False
       }
connection = ConnectHandler(**cisco_device)
print('Entering the enable mode...')
connection.enable()

print('Sending commands from file ...')
output = connection.send_config_from_file('hardening.txt')
print(output)

print('Closing connection')
connection.disconnect()
