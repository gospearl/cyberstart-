import socket

clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsock.connect(('localhost', 12345))

# Create a socket and bind it to a specific address and port
serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.bind(('localhost', 12345))
serversock.listen(1)

print("Waiting for a connection...")
clientsock, addr = serversock.accept()
print("Connected to", addr)

clientsock.send("Welcome to Maths_Server 1.0\n")

try:
    clientsock.send("Enter the first number, so I can EVALuate it:\n")
    firstNum = eval(clientsock.recv(1024))
    firstNum = firstNum + firstNum + ord(flag[4]) + ord(flag[8]) + ord(flag[5])
    clientsock.send("Enter the second number, so I can EVALuate it:\n")
    secondNum = eval(clientsock.recv(1024))
    if secondNum == firstNum:
        # Instead of sending the flag to the client, print it on the server
        print("The flag is:", flag)
        firstNum = 0
        secondNum = 0
except:
    pass
