import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host, port))
s.send("hello server")
s.close()
