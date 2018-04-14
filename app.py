#!/usr/bin/python

import sys
import paramiko
import getpass

hosts = raw_input('Enter Your Hostname or Host IP: ')
user = raw_input('Enter Your Login Username: ')
password = getpass.getpass('Enter Your Login Password: ')
command = raw_input("Enter target command:")

ssh = paramiko.SSHClient() #Define value 'ssh' as calling the paramiko.sshclient
#print('calling paramiko')
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Must come before connect line to add hosts to known_hosts
#ssh.connect("name", username="user", password="passwd")
ssh.connect(hostname = hosts, username = user, password = password) # key_filename means to specify the actual file, pkey on the
#other hand means to actually paste in the key text itself
print('trying to connect')
ssh.invoke_shell()
stdin, stdout, stderr = ssh.exec_command (command)
print(stdout.read())
#ssh.close()
#Dev Branch
