#!/bin/python2

import socket
import ssl
import time
import os

s = socket.socket()	
ssl_sock = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1, 
		ca_certs="./certs/server.crt", cert_reqs=ssl.CERT_REQUIRED )

host = socket.gethostname()	 
port = 10000

ssl_sock.connect((host, port))
print repr(ssl_sock.getpeername())

d_start = time.time()
with open('received_file', 'wb') as f:
    while True:
        data = ssl_sock.recv(2048)
        if not data:
           	break
        f.write(data)
f.close()
ssl_sock.close()
d_end = time.time() - d_start

size = os.path.getsize("received_file")
print("Size:\t\t" + str(size))
print("Time Download:\t" + str(d_end))
d_speed = ((size/1024)/1024)/d_end
print("Download:\t" + str(d_speed) + " MB/s")
os.remove("received_file")