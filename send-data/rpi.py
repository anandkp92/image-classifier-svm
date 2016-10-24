import threading
import socket
import time

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
	s = socket.socket()
	host = socket.gethostname()
	sendPort = 12345

	try:
		s.connect((host, sendPort))
	except:
		s.close()
		time.sleep(10)
		sendData(threadName)
	print "src:rpi connected to destn:server"
	i = 0
	while True:
		s.send("hello server "+str(i) +" from "+threadName)
		i+=1
		time.sleep(5)

	s.close()

def recvData(threadName):
	s = socket.socket()
	host = socket.gethostname()
	port = 12346
	s.bind((host, port)) 
	s.listen(5)

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

thread1 = sendThread(1, "sendThread-rpi")
#thread2 = recvThread(2, "recvThread-rpi")

thread1.start()
#thread2.start()