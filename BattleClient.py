# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 08:42:16 2019

@author: wallacek2
"""
import _thread
import socket

# set up client
host = input('Enter server host: ')
if not host:
    host = "localhost"

port = input('Enter server port: ')
if not port:
    port = 10000
else:
    port = int(port)
    
# connect socket to server
servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servsock.connect((host, port))





