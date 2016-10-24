import threading
import socket
import time
import sys
import numpy
import pickle
import binascii

class sendThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        	sendData(self.name)

class recvThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        	recvData(self.name)

def sendData(threadName):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#host = socket.gethostname()
	host = '192.168.43.121'
	sendPort = 1234

	try:
		print "connecting..."
		s.connect((host, sendPort))
	except Exception, e:
		print "connection failed ", str(e)
		s.close()
		time.sleep(10)
		sendData(threadName)
	print "src:server connected to destn:rpi"
	i = 0
	while True:
		try:
			s.send("hello rpi "+str(i) +" from "+threadName)
			i+=1
			time.sleep(5)
		except:
			print "cannot send"

	s.close()


def recvData(threadName):
	s = socket.socket()
	#host = socket.gethostname()
	host = '192.168.43.36'
	port = 12345
	s.bind((host, port)) 
	s.listen(5)

	try:
		c, addr = s.accept()
		print "got connection from ", addr, threadName
	except:
		time.sleep(5)
		recvData(threadName)
	#while True:
	l = c.recv(1024)

		# buf = 
	print l
	l = c.recv(int(l))
	n = pickle.loads(l)
	
	print n

		#unpickled_data = pickle.loads(l)
		#print unpickled_data
		
	s.close()

#thread1 = sendThread(1, "sendThread-server")
thread2 = recvThread(2, "recvThread-server")

#thread1.start()
thread2.start()