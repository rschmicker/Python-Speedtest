#!/bin/python2

import socket
import ssl

# generate file 
mb_size = 50
f = open("upload","wb")
f.seek(mb_size*1024*1024)
f.write("\0")
f.close()

# server conn info
host = socket.gethostname()
port = 10000

# set up socket
s = socket.socket()
s.bind((host, port))
s.listen(5)

print "Server listening...."

while True:
	conn, addr = s.accept()
	ssl_conn = ssl.wrap_socket(conn, server_side=True, 
			certfile="./certs/server.crt", keyfile="./private/server.key")
	filename='upload'
	f = open(filename,'rb')
	l = f.read(1024)
	while (l):
	   ssl_conn.send(l)
	   l = f.read(1024)
	f.close()

	print('Done sending')
	ssl_conn.shutdown(socket.SHUT_RDWR) # added to make sure it flushes data
	ssl_conn.close()