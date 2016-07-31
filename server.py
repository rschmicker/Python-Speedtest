import socket

mb_size = 50
f = open("upload","wb")
f.seek(mb_size*1024*1024)
f.write("\0")
f.close()

port = 10000
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(5)

print "Server listening...."

while True:
	conn, addr = s.accept()
	filename='upload'
	f = open(filename,'rb')
	l = f.read(1024)
	while (l):
	   conn.send(l)
	   l = f.read(1024)
	f.close()

	print('Done sending')
	conn.close()