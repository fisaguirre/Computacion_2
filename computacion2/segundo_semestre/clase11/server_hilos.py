#!/usr/bin/python
import threading
import socket
import os
desc= socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
"""para que no diga address already in use"""


#desc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def fun1(newdesc):
    leido = newdesc.recv(2048)
    print leido
    while (leido[0:4] != "exit"):
        print leido
        newdesc.send(leido.upper()[::-1])
        newdesc.send("\n")
        leido = newdesc.recv(2048)
    newdesc.close()



#servidor=raw_input("mi ip:")
#port=raw_input("mi port:")
#desc.bind((servidor, int(port)))

#192.168.2.154
#ifconfig
#desc.bind(("192.168.14.250", 5000))
desc.bind(("127.0.0.1", 5000))

desc.listen(20)
while True:
    newdesc,cli = desc.accept()
    print cli
    t1 = threading.Thread(name="h1", target=fun1, args=(newdesc,))
    t1.start()

