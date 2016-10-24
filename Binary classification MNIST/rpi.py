import threading
import socket
import time
import digit_recognition
import marshal
import pickle
import binascii
class sendThread (threading.Thread):
    def __init__(self, threadID, name, x):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
	self.x = x
    def run(self):
        	sendData(self.name, self.x)

class recvThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        	recvData(self.name)

def sendData(threadName, x):
	s = socket.socket()
	#host = socket.gethostname()
	host = '192.168.43.36'
	sendPort = 12345

	try:
		s.connect((host, sendPort))
	except:
		s.close()
		time.sleep(10)
		sendData(x)
	print "src:rpi connected to destn:server"
	#i = 0
	#while True:
	s.send(x)
	#i+=1
		#time.sleep(5)

	s.close()

def recvData(threadName):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	#host = socket.gethostname()
	host = '192.168.43.121'
	#host = socket.gethostbyname(socket.gethostname())
	port = 1234
#	s.bind((host, port))
	'''
	while True:
		#time.sleep(5)
		data, addr = s.recvfrom(1024)
		print data
	'''
	try:
		s.bind((host, port)) 
		print "binded"
		s.listen(5)
	except:
		print "bind failed"
		time.sleep(3)
		recvData(threadName)

	try:
		c, addr = s.accept()
		print "got connection from ", addr, threadName
	except:
		time.sleep(5)
		recvData(threadName)
	while True:
		l = c.recv(1024)
		if(l):
			print l
	s.close()
	
 
X = pickle.dumps(binascii.hexlify(digit_recognition.parse_images("train-images-idx3-ubyte")))
y = pickle.dumps(digit_recognition.parse_labels("train-labels-idx1-ubyte"))

#X = [1,2,3,4,111,6,7,8,9,10]
#print X
#thread2 = recvThread(2, "recvThread-rpi")
thread1 = sendThread(1, "sendThread", X)
thread1.start()
#thread2.start()
