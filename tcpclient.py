from socket import *
import threading

HOST = "127.0.0.1"
PORT = 50007

def recv ():
    while 1:
        res = serverSocket.recv(1024).decode()#Bloqueia a exec até receber
        print("server: " + res)

serverSocket = socket()
serverSocket.connect((HOST,PORT))
rcvThread = threading.Thread(target=recv)
rcvThread.start()

while 1:
    msg = input('')
    
    if msg == "exit":
        serverSocket.close()
        break

    serverSocket.send(msg.encode('utf-8'))
      
    
    

