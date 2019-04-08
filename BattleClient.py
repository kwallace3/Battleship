# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 08:42:16 2019

@author: wallacek2
"""
import _thread
import socket

# set up client
port = 10000
IP = input('Enter server host: ')
if not IP:
    IP = "localhost"

# connect socket to server
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect((IP, port))

# initiate gameplay
waiting = True
while waiting:
    client = input("Welcome to Battleship! Please type your name and press ENTER to continue... ")
    waiting = False

print ("Please place your ships on the board. Once finished, press ENTER to continue...")






