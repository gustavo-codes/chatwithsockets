from socket import *

HOST = "127.0.0.1"
PORT = 50007

serverSocket = socket()
serverSocket.connect((HOST,PORT))
while 1:
    msg = input('')
    
    if msg == "exit":
        serverSocket.close()

    serverSocket.send(msg.encode('utf-8'))
    res = serverSocket.recv(1024).decode()#Bloqueia a exec até receber
    print("server: " + res)
    

