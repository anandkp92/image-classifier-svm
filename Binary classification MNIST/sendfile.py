import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = socket.gethostname()
host = '192.168.43.36'
sendPort = 12345

	#try:
	#print "connecting..."
s.connect((host, sendPort))
	#except Exception, e:
	#print "connection failed ", str(e)
	#s.close()
	#time.sleep(10)
#sendData(threadName)
#	print "src:server connected to destn:rpi"
#	i = 0
#	while True:
#	try:
#	s.send("hello rpi "+str(i) +" from "+threadName)
#	i+=1
#time.sleep(5)
#	except:
#	print "cannot send"

#s.close()
filename = "/home/pi/Documents/image-classifier-svm/Binary classification MNIST/train-images-idx3-ubyte.gz"
file_size = str(os.stat(filename).st_size)
print file_size
s.send(file_size)
work_file = open(filename, "rb")
file_size = int(file_size)
while (file_size>0):
	buf = work_file.read(1024)
	s.send(buf)
	file_size-=1024
	print file_size
print "done"
