### http_server_template.py

# Import socket module
from socket import *        

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

#Get from user a port number, and assign to the socket

###Your Code
serverPort=int(raw_input("Server Port: "))

# Bind the socket to server address and server port

###Your Code
serverSocket.bind(("",serverPort))

# Start listening to at most 1 connection at a time
serverSocket.listen(1)

# Server should be up and running and listening to the incoming connections
while True:
    print 'Ready to serve...'

    # Set up a new connection from the client
    ###Your Code
    connectionSocket, addr = serverSocket.accept()

    # If an exception occurs during the execution of try block
    # the rest of the block is skipped
    # If the exception type matches the word after "except" statement
    # the except clause is executed
    try:
        # Receives the request message from the client
        message =  connectionSocket.recv(1024)

        # You can print this message to see how an http request looks like.
        # Request format is specified in the http RFC
        # Write code to print incoming http request

        ###Your Code
        print ("Received From Client: ", message)

        # Extract the path of the requested file from the message
        # If you split the message into tokens, the filename will be the second token
        # The path is the second part of HTTP header, identified by index [1]

        filename = message.split()[1]

        # This filename will incluse  a character '/' in the beginning, so
        # you need to read the path from the second character onwards to get the filename
        # or otherwise get rid of the leading '/'

        ###Your Code
        i=len(filename)
        j=1
        name=filename[j:i]
        print("FileName: ", name)
        fileO = open(name)

        # Store the entire content of the requested file in a temporary buffer

        outputdata = fileO.read()

        # Send the HTTP response header line to the connection socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")

        # Send the content of the requested file to the connection socket

        ###Your Code
        for p in range(0,len(outputdata)):
            connectionSocket.send(outputdata[p])
        # Close the client connection socket

        ###Your Code
        connectionSocket.close()

    except IOError:
        # Send HTTP response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
        connectionSocket.send("<html><head></head><body><h1>404 Not Found - Please Check your filename!</h1></body></html>\r\n")
        # Close the client connection socket

        ###Your Code
        connectionSocket.close()

# close the server socket

###Your Code
serverSocket.close()

                
