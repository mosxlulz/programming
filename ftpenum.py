#!/usr/share/python
import socket,sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], 21))
s.send ("USER anonymous\r\n")
resp = s.recv(1024)
print resp

s.send ("PASS anonymous\r\n")
s.send ("PWD\r\n")
resp = s.recv(2048)
print resp
