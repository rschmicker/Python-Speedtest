#!/usr/bin/python		   # This is client.py file
import socket				   # Import socket module
import time
import os

s = socket.socket()			 # Create a socket object
host = socket.gethostname()	 # Get local machine name
port = 40000					# Reserve a port for your service.

s.connect((host, port))

d_start = time.time()

with open('received_file', 'wb') as f:
	print 'file opened'
	while True:
		#print('receiving data...')
		data = s.recv(1024)
		#print('data=%s', (data))
		if not data:
			break
		# write data to a file
		f.write(data)
d_end = time.time() - d_start
"""
l = f.read(1024)
while (l):
	conn.send(l)
       #print('Sent ',repr(l))
	l = f.read(1024)
	f.close()
"""
size = os.path.getsize("received_file")
print("Size:\t" + str(size))
print("Time Download:\t" + str(d_end))
speed = ((size/1024)/1024)/d_end
print("Download:\t" + str(speed) + " MB/s")
f.close()
s.close()
print('connection closed')
