#!/usr/bin/python

import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_polocy(paramiko.AutoAddPolicy())
#Username and password are passed as arguments 
client .connect(hostname=sys.argv[1], port='22', username=sys.argv[2], password=sys.argv[3])
#Passing commands to extract IP's and Macs
stdin0, stdout0, stderr0 = client.exec_command('cat /etc/sysconfig/network-scripts/ifcfg-eth0')
stdin1, stdout1, stderr1 = client.exec_command('cat /sys/class/net/eth0/address')
stdin2, stdout2, stderr2 = client.exec_command('cat /etc/sysconfig/network-scripts/ifcfg-eth1')
stdin3, stdout3, stderr3 = client.exec_command('cat /sys/class/net/eth1/address')

#Extracting MAC's and IP's


ip_0 = stdout0.readlines()

for line0 in ip_0:
    if 'IPADDR' in line0:
        IP_0=line0.strip().split('=')
        eth0ip=IP_0[1]

mac0 = stdout1.read()

ip_1 = stdout2.readlines()
for line1 in ip_1:
    if 'IPADDR' in line1:
        IP_1=line1.strip().split('=')
        eth1ip=IP_1[1]

mac1 = stdout3.read()
#printing eth0, eth1 ip and mac addresses
print('  **eth0ip==> '+eth0ip+ '  **eth0mac==> '+mac0+ '  **eth1ip==> '+eth1ip+ '  **eth1mac==> '+mac1)
client.close()