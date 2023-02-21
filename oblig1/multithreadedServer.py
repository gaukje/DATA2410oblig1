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