"""
Task 1: Making a simple webserver
You will develop a web server that handles one HTTP request at a time. Your web server should
accept and parse the HTTP request, get the requested file from the server’s file system, create an
HTTP response message consisting of the requested file preceded by header lines, and then send the
response directly to the client. If the requested file is not present in the server, the server should send
an HTTP “404 Not Found” message back to the client
"""
# import socket module
from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)  # Server socket
serverPort = 6789
serverHost = '127.0.0.1'
serverSocket.bind(('', serverPort))

serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    try:
        # Receive the request message from the client
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        # the name of the file includes "/", to remove it, [1:] is used to slice the file name from the second character
        outputdata = f.read()
        f.close()

        # Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
        connectionSocket.send('Content-Type: text/html\r\n'.encode())
        connectionSocket.send(('Content-Length: %d\r\n' % len(outputdata)).encode())
        connectionSocket.send('\r\n'.encode())

        # Send the content of the requested file to the client

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()

    except IOError:
        # Send response message for file not found
        connectionSocket.close()
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())
        connectionSocket.send('Content-Type: text/html\r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        connectionSocket.send('<html><body><h1>404 Not Found</h1></body></html>\r\n'.encode())

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding da
