#!/usr/bin/python		   # This is server.py file
import socket                   # Import socket module
import os

f = open('upload_test',"wb")
f.seek(36700160)
f.write("\0")
f.close()

port = 40000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print 'Server listening....'

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    #data = conn.recv(1024)
    #print('Server received', repr(data))

    filename='upload_test'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       #print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send('Thank you for connecting')
    conn.close()

os.remove("upload_test")