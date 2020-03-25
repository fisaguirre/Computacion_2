#!/usr/bin/python

import socket
import os
desc= socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
#para que no diga address already in use
desc.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)

servidor=raw_input("mi ip:")
port=raw_input("mi port:")
desc.bind((servidor, int(port)))
#192.168.2.154
#ifconfig
#desc.bind(("192.168.14.250", 5000))
desc.listen(20)
while True:
    print ("hola")
    newdesc,cli = desc.accept()
    print cli
    pid = os.fork()
    if pid == 0:
        leido = newdesc.recv(2048)
        print leido
        while (leido[0:4] != "exit"):
            print leido
            newdesc.send(leido.upper()[::-1])
            newdesc.send("\n")
            leido = newdesc.recv(2048)
        exit()
    newdesc.close()

