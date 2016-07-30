#!/usr/bin/python           # This is client.py file

import socket                   # Import socket module
import time
import os

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 20000                     # Reserve a port for your service.

s.connect((host, port))

with open('received_file', 'wb') as f:
    print 'file opened'
    t_start = time.time()
    print(t_start)
    while True:
        data = s.recv(1024)
        print(data)
        if not data:
            break
        # write data to a file
        f.write(data)
t_end = time.time() - t_start
print(t_end)
t_total = (t_end)/60
size_of_file = os.path.getsize("received_file")
f.close()
print("Download:\t" + str(size_of_file/t_total))
s.close()
print('connection closed')