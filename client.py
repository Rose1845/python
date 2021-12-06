from os import close
import socket
s=socket.socket()
host=socket.gethostname()
port=12345


s.connect((host,port))
s.recv(1024)
s.close()