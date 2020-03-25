#!/usr/bin/python
import socket

desc= socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
#servidor=raw_input("server:")
#port=raw_input("port:")

#desc.connect(("192.168.14.250", "5000"))
#desc.connect(("127.0.0.1", 5000))
desc.connect(("192.168.14.250", 5000))

consulta=raw_input("consulta:")
desc.send(consulta+"\n")
leido = desc.recv(2048)
print leido,
while leido != '':
    leido = desc.recv(2048)
    print leido,


""" nc -lu 192.168.14.250 5000"""
"""192.168.14.250 5000"""