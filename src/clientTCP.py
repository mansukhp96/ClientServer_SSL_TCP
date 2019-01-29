#!/usr/bin/env python

import socket                                          # import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating a socket
port = 27995                                           # port number
host_ip = socket.gethostbyname(sys.argv[1])  # getting host ip
s.connect((host_ip, port))
hello = b'cs5700spring2019 HELLO ' + str(sys.argv[2]) + '\n'  # HELLO message to server
s.send(hello)
while True:                                            # loop to get the SOLUTION
    data = s.recv(1024)
    # print data                                       #prints all the equations the server sends
    p = data.split()                                   # splitting data
    if p[2] == 'BYE':
        print
        p[1]     # to print secretflag
        break
    else:
        g = eval(p[2] + p[3] + p[4])                   # eval to find the SOLUTION
        h = b'cs5700spring2019 ' + str(g) + '\n'       # sending the SOLUTION
        s.send(h)
s.close()                                              # close the connection
