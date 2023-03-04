"""
Task 2: Making a web client
Instead of using a browser, write your own HTTP client to test your server. Your client will connect
to the server using a TCP connection, send an HTTP request to the server, and display the server
response as an output. You can assume that the HTTP request sent is a GET method. The client
should take command line arguments specifying the server IP address or host name, the port at which
the server is listening, and the path at which the requested object is stored at the server. The following
is an input command format to run the client. client.py server host server port filename
"""

import sys
from socket import*

# Checking if the correct amount of input arguments is provided
if len(sys.argv) != 4:
    print("Usage: python client.py <host> <port> <fileName>")
    sys.exit()

# Assigning variablies to command line arguments
serverHost = sys.argv[1]
serverPort = int(sys.argv[2])
filename = sys.argv[3]

# TCP client socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connecting to server with predefined host and port
clientSocket.connect((serverHost, serverPort))

# Sending the HTTP get request to the server
request = "GET /" + filename + " HTTP/1.1\r\nHost: " + serverHost + "\r\n\r\n"
clientSocket.send(request.encode())

# Receiving HTTP response form server
message = b''       # byte string
while True:         # Loop that receives data
    data = clientSocket.recv(2048)
    if not data:
        # No more data ro receive
        break
    message += data         # Appending data to message

# Printing message
print(message.decode())

# Closing socket
clientSocket.close()
sys.exit()
