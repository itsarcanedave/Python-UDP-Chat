import socket

ip = socket.gethostbyname(socket.gethostname())
print ("Server is online at", ip)
port = int(input ("Enter port: "))
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((ip, port))
print ("Listening on port", port)

while True:
    data, addr = serverSock.recvfrom(1024)
    dataString = data.decode()
    print ("Message: ", dataString)
  