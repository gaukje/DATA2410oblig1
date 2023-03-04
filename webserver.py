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


def handle_requests(connectionSocket):
    try:
        # Receive the request message from the client
        message = connectionSocket.recv(2048).decode()
        filename = message.split()[1][1:]
        # the name of the file includes "/", to remove it, [1:] is used to slice the file name from the second character
        with open(filename, 'rb') as f:         #Open file in "binary mode" - read content as bytes
            outputdata = f.read()               #Read content of filename as f


        # Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())               #HTTP response status line
        connectionSocket.send('Content-Type: text/html\r\n'.encode())
        connectionSocket.send(('Content-Length: %d\r\n' % len(outputdata)).encode())
        connectionSocket.send('\r\n'.encode())                          #End of the response header

        # Send the content of the requested file to the client

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i:i + 1])
            # Loop that sends characters from outputdata one byte at a time from 0 to the length of outputdata

    except IOError:
        # Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())   #HTTP response status if there are errors trying to run the code above
        connectionSocket.send('Content-Type: text/html\r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        connectionSocket.send('<html><body><h1>404 Not Found</h1></body></html>\r\n'.encode())
    finally:
        connectionSocket.close()        #Ensuring that the program exits


serverSocket = socket(AF_INET, SOCK_STREAM)  # Server socket
serverPort = 6789                            #Server port
serverHost = '127.0.0.1'                       #Server host
serverSocket.bind(('', serverPort))             #Associating server socket with specific network interface

serverSocket.listen(5)                      #Maximum number of queued connecteiions

# Establish the connection
while True:
    #Loop that listens for incoming connections
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    #Create a new thread that handles requests
    t = threading.Thread(target=handle_requests, args=(connectionSocket,))
    t.start()
