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
# Request all encoded messages from the server
while True:
    message = "get"
    clientSocket.sendall(message.encode())

    # Receive the response from the server
    response = clientSocket.recv(1024).decode()

    # Check if there are no more messages
    if response == "no more messages":
        break

    # Print the encoded message
    print(response)

clientSocket.close()
#request += "GET /" + filename + " HTTP/1.1\r\nHost: " + serverHost + "\r\n\r\n"

#clientSocket.send(request.encode())

# Receiving HTTP response form server
response = clientSocket.recv(2048)

# Printing message
print(response.decode())

# Closing socket
clientSocket.close()
sys.exit()