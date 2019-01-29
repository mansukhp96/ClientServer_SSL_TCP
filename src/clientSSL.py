#!/usr/bin/env python

import socket  # Import socket
import sys
import ssl  # Import ssl

sl = ssl.SSLContext(ssl.PROTOCOL_SSLv23)               # setting the context

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating the socket
port = 27996                                           # port number for ssl connection
host_ip = socket.gethostbyname(str(sys.argv[2]))       # getting the IP from hostname provide din parameter
wrappeds = sl.wrap_socket(s)                           # wrapping the socket for ssl
wrappeds.connect((host_ip, port))
hello = b'cs5700spring2019 HELLO ' + str(sys.argv[3]) + '\n'  # taking the NUID from the parameter and sending HELLO
wrappeds.send(hello)
while True:                           # loop to solve the solution and get secret flag
    data = wrappeds.recv(1024)
    # print data				      #prints all the equations sent by the server
    p = data.split()
    if p[2] == 'BYE':
        print
        p[1]                          # prints the single line secret flag
        break
    else:
        g = eval(p[2] + p[3] + p[4])  # evaluates the equation sent by the server
        h = b'cs5700spring2019 ' + str(g) + '\n'
        wrappeds.send(h)
wrappeds.close()
