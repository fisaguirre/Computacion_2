#!/usr/bin/python
#El par de caracteres #! indica al sistema operativo que dicho script se debe ejecutar utilizando el intérprete especificado a continuación

import os
import time
print "hola mundo"

pid = os.fork()

if pid == 0: #hijo
    print "soy el hijo",os.getpid(), os.getppid()
    os._exit(0)
else:
    print "soy el padre",os.getpid(), os.getppid()

os.waitpid(pid,0)

print "mi hijo termino"