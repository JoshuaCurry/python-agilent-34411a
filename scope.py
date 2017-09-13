# Agilent SCPI Data Utility
# Josh Curry 2017
#
# Set up your instrument and run this program to read data 
# as fast as possible to file.


import socket
from datetime import datetime
import atexit

HOST = '192.168.1.10'
PORT = 5025
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def readout():
	print "Writing data to file..."
	f.write('\n'.join(dat))
	print "Closing File...."
	f.close()
	exit()

atexit.register(readout)

thefile = "reading-"+str(datetime.now()).replace(" ", "-")+".txt"
print "Opening " + thefile

f = open(thefile, "w")
i = 0

dat = []

print "Reading from instrument to RAM..."
print "Press CTRL-C to stop"
while 1:
	s.sendall("READ?\r\n")
	data = s.recv(1024)
	i = i + 1	
	dat.append(data.rstrip())
s.close()
