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
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a sever socket
    # Write your code here
    # End of your code
while True:
    # Establish the connection print('Ready to serve...') connectionSocket, addr =
    try:
    # Write your code here
    # End of your code
    message =  # Write your code here #End of your code
    filename = message.split()[1]
    f = open(filename[1:])
    outputdata =  # Write your code here #End of your code
    # Send one HTTP header line into socket
    # Write your code here
    # End of your code
    # Send the content of the requested file to the client
    for i in range(0, len(outputdata)):
        connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Write your code here
        # End of your code
        # Close client socket

        # Write your code here
        # End of your code
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding da