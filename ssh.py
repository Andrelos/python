#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys, paramiko



hostname = ""
password = ""
command = "uname -a"

username = "root"
port = 22


client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
client.connect(hostname, port=port, username=username, password=password)

stdin, stdout, stderr = client.exec_command(command)
print stdout.read(),
