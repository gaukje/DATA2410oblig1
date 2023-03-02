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

if len(sys.argv) != 4:
    print("Usage: python client.py <serverName> <serverPort> <fileName>")
    sys.exit()
"""
sys.argv is a list in Python that contains the command-line arguments passed to the script. When a Python script is 
executed, the command-line arguments passed are stored in the sys.argv list.
"""
serverHost = sys.argv[1]
serverPort = int(sys.argv[2])
filename = sys.argv[3]

# TCP client socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connecting to server
clientSocket.connect((serverHost, serverPort))

# Sending the HTTP get request to the server
request = "GET /" + filename + " HTTP/1.1\r\nHost: " + serverHost + "\r\n\r\n"
clientSocket.send(request.encode())

# Receiving HTTP response form server
message = b''
while True:
    data = clientSocket.recv(2048)
    if not data:
        # No more data ro receive
        break
    message += data

# Printing message
print(message.decode())

# Closing socket
clientSocket.close()
sys.exit()
