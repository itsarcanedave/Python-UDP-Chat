import socket
import ipaddress

name =  input ("Please enter your name: ")
print ("Hello", name, "!")
local = socket.gethostbyname(socket.gethostname())
print ("Your client IP address is", local)
ip = input ("Please enter server IP address: ")
ipaddress.ip_address(ip)
port = int(input ("Please enter port: "))

counter = 1
while (counter <= 3):
    if counter <=2:
        messageString = input("Enter a message: ")
        separator = str(": ")
        username = str.encode(name)
        separatorSend = str.encode(separator)
        message = str.encode(messageString)
        sendMessage = username + separatorSend + message
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        clientSocket.sendto(sendMessage, (ip, port))
        data, server = clientSocket.recvfrom(4096)
        dataString = data.decode()
        print (dataString)
        counter = counter + 1
    elif counter == 3:
        messageString = input("Enter a message: ")
        separator = str(": ")
        username = str.encode(name)
        separatorSend = str.encode(separator)
        message = str.encode(messageString)
        sendMessage = username + separatorSend + message
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        clientSocket.sendto(sendMessage, (ip, port))
        break

print ("Connection closed!")     
done = input("Press any key to exit!")
        