import socket
import ipaddress

ip = input ("Enter server IP address: ")
ipaddress.ip_address(ip)
port = int(input ("Enter port: "))
while(True):
    messageString = input("Enter a message: ")
    message = str.encode(messageString)
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSock.sendto(message, (ip, port))
