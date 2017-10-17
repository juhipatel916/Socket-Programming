### http_client_template.py

# Import socket module
from socket import *
import httplib


serverName=raw_input("Server Name/IP: ")
serverPort=int(raw_input("Server Port: "))
fileName  = raw_input("File to get from server: ")
fileToWrite=raw_input("File to write data from server: ")

# Create a TCP server socket, connect it to the port # given
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)

###Your Code
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

# Now compose an http request header for a GET request, including the file to get
# Include in the header meta-data fields  "User-agent" and "From"
# For User-agent give "Python" and for From give your email.
# Make sure the header has two new line characters (\n) at the end.

### Your Code
s="get /"+fileName+" HTTP/1.0 User-agent:Python From:patelj6@hawkmail.newpaltz.edu\n\n"

# Send the request through the socket

### Your Code
clientSocket.send(s)
# Open the local file to which incoming data (server's response)  is to be written. 
# Receive the bytes from the socket, write to file and the console.
# if incoming data has length 0, break.
# Close the opened local file.


### Your Code
fp=open(fileToWrite, "w")
while True:
    resp = clientSocket.recv(1024)
    if resp == "": break
    print resp
    fp.write(resp)
fp.close()

# Close the socket connection

### Your Code
clientSocket.close()