from socket import *
import threading

HOST = "127.0.0.1"
PORT = 50007

def recv ():
    while 1:
        req = connectionSocket.recv(1024).decode('utf-8')#Bloqueia a exec até receber
        print("client: " + req)

serverSocket = socket(AF_INET,SOCK_STREAM) #AF_INET IPV4, SOCK_STREAM TCP
serverSocket.bind(('',PORT))
serverSocket.listen(1)
while 1:
    connectionSocket,addr = serverSocket.accept()
    print("Connected to: ")
    print(addr)

    rcvThread = threading.Thread(target=recv)
    rcvThread.start()
    while 1:
        res = input("")

        if res == "exit":
            connectionSocket.close()

        connectionSocket.send(res.encode())
        
    

