#!/usr/bin/python
#El par de caracteres #! indica al sistema operativo que dicho script se debe ejecutar utilizando el intérprete especificado a continuación

import os
import signal
#señales
print os.getpid()
pid = os.fork()

if (pid == 0):
    os.execv("/bin/ps", ("/bin/ps","-f"))
    print "porque no sale esto?"

    os._exit(0)

os.waitpid(pid,0)
