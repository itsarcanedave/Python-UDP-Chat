import socket

ip = socket.gethostbyname(socket.gethostname())
print ("Server is online at", ip)
port = int(input ("Enter port: "))
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((ip, port))
print ("Listening on port", port)


counter = 1
while (counter <= 3):
    if counter == 1:
        data, address = serverSocket.recvfrom(1024)
        dataString = data.decode()
        print (dataString)
        firstMessage = str("Server: Who's there?")
        firstReply = str.encode(firstMessage)
        reply = serverSocket.sendto(firstReply, address)
        counter = counter + 1
    elif counter == 2:
        data, address = serverSocket.recvfrom(1024)
        dataString = data.decode()
        print (dataString)
        secondMessage = dataString.partition(":")[2]
        strippedMessage = secondMessage.lstrip()
        strippedEncode = str.encode(strippedMessage)
        serverID = str("Server: ")
        serverMessage = str.encode(serverID)
        who = str(" who?")
        whoMessage = str.encode(who)
        secondReply = serverMessage + strippedEncode + whoMessage
        reply = serverSocket.sendto(secondReply, address)
        counter = counter + 1
    elif counter == 3:
        data, address = serverSocket.recvfrom(1024)
        dataString = data.decode()
        print (dataString)
        break

print ("Connection closed!")     
done = input("Press any key to exit!")
      
  