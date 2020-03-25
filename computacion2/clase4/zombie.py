#! /usr/bin/python

import os
import time
print "hola mundo"
for hijo in range(5):
    pid = os.fork()
    if pid == 0:
        print "soy el hijo",os.getpid(), os.getppid()
        os._exit(0) # exit status

    
print "soy el padre",os.getpid(), os.getppid()
leido = os.read(0,1000)
print "chau, mi hijo termino"