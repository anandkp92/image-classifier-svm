import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port)) 
s.listen(5)

while True:
	c, addr = s.accept()
	print "got connection from ", addr
	l = c.recv(1024)
	if(l):
		print l
		break
s.close()


#s.connect((host, port))
#s.send("hello server")
#s.close()
