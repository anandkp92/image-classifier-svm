import socket 

s = socket.socket()
#host = socket.gethostname()
host = '192.168.43.36'
port = 12345
s.bind((host, port)) 
s.listen(5)


c, addr = s.accept()
file_size = int(c.recv(1024))
print file_size

f = open("new_file.gz", "wb+")
while file_size>0:
	work_file = c.recv(1024)
	f.write(work_file)
	file_size-=len(work_file)
f.close()
