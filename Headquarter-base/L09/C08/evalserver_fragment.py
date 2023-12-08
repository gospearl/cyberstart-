clientsock.send("Welcome to Maths_Server 1.0\n")

try:
    clientsock.send("Enter the first number, so I can EVALuate it:\n")
    firstNum = eval(clientsock.recv(1024))
    firstNum = firstNum + firstNum + ord(flag[4]) + ord(flag[8]) + ord(flag[5])
    clientsock.send("Enter the second number, so I can EVALuate it:\n")
    secondNum = eval(clientsock.recv(1024))
    if secondNum == firstNum:
        clientsock.send("The flag is: " + flag + "\n")
        firstNum = 0
        secondNum = 0
except:
    pass

clientsock.close()
