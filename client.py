import socket
import time
import os

s = socket.socket()			 
host = socket.gethostname()	 
port = 10000

s.connect((host, port))

d_start = time.time()
with open('received_file', 'wb') as f:
    while True:
        data = s.recv(1024)
        if not data:
            break
        f.write(data)
f.close()
s.close()
d_end = time.time() - d_start

size = os.path.getsize("received_file")
print("Size:\t\t" + str(size))
print("Time Download:\t" + str(d_end))
d_speed = ((size/1024)/1024)/d_end
print("Download:\t" + str(d_speed) + " MB/s")
os.remove("received_file")