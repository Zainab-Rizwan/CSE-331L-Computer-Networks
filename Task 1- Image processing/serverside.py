from socket import *
from PIL import Image
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen()
print("Server is ready to receive")
while (1):
    connectionSocket, addr = serverSocket.accept()
    file = connectionSocket.recv(2048)
    img=Image.open(f"{file.decode()}")
    img.show()
connectionSocket.close()     