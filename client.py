#!/usr/bin/env python

import socket


TCP_IP = "127.0.0.1"
TCP_PORT = 5005
BUFFER_SIZE = 20
MESSAGE = "Hello"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
for i in MESSAGE:
    s.send(i.encode("utf-8"))
    data = s.recv(BUFFER_SIZE)
    print("received data: ", data)
s.close()
