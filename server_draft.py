"""
Task 3: Making a multi-threaded web server
Currently, your web server handles only one HTTP request at a time. You should implement a
multithreaded server that is capable of serving multiple requests simultaneously. Using threading, first
create a main thread in which your modified server listens for clients at a fixed port. When it receives
a TCP connection request from a client, it will set up the TCP connection through another port and
1
services the client request in a separate thread. There will be a separate TCP connection in a separate
thread for each request/response pair.
"""

import threading
# import socket module
from socket import *
import sys


def handle_requests(connectionSocket):
    try:
        # Receive the request message from the client
        message = connectionSocket.recv(2048).decode()
        filename = message.split()[1][1:]
        # f = open(filename[1:])
        # the name of the file includes "/", to remove it, [1:] is used to slice the file name from the second character
        with open(filename, 'rb') as f:
            outputdata = f.read()
        # f.close()

        # Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
        connectionSocket.send('Content-Type: text/html\r\n'.encode())
        connectionSocket.send(('Content-Length: %d\r\n' % len(outputdata)).encode())
        connectionSocket.send('\r\n'.encode())

        # Send the content of the requested file to the client

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i:i + 1])
            # Loop that sends characters from outputdata
            """
            In Python, when you slice a string or a sequence, you can use the start:stop:step notation. 
            The i:i+1 slice notation used in outputdata[i:i+1] creates a new sequence containing a single element, 
            which is the ith element of outputdata.

            The reason why the slice notation is used here is that connectionSocket.send() requires a bytes-like 
            object as its input. outputdata is a string, so each character must be converted to a byte using the encode()
            method before it is sent.

            Alternatively, outputdata[i:i+1].encode() could be used instead of outputdata[i:i+1], which would encode 
            each slice as bytes before sending it to connectionSocket.send().

            """
    except IOError:
        # Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())
        connectionSocket.send('Content-Type: text/html\r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        connectionSocket.send('<html><body><h1>404 Not Found</h1></body></html>\r\n'.encode())
    finally:
        connectionSocket.close()


serverSocket = socket(AF_INET, SOCK_STREAM)  # Server socket
serverPort = 6789
serverHost = '127.0.0.1'
serverSocket.bind(('', serverPort))

serverSocket.listen(5)

# Establish the connection
while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    t = threading.Thread(target=handle_requests, args=(connectionSocket,))
    t.start()

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding da
