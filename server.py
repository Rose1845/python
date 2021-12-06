from os import close
import socket

s=socket.socket()#create socket object
host=socket.gethostname()#gte local machine
port=12345
s.bind((host,port))#bind to the port


s.listen(5)#waits for client connection
while True:
    c,addr=s.accept()#establisj connection with client
    print('Got connection from',addr)
    c.send('Thank you for connecting')
    c.close()
