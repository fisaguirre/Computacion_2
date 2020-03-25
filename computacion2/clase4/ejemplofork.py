#!/usr/bin/python
#El par de caracteres #! indica al sistema operativo que dicho script se debe ejecutar utilizando el intérprete especificado a continuación

import os

print "primero"

pid1 = os.fork()

print "segundo",pid1,os.getpid(),os.getppid()

pid2 = os.fork()
print "tercero",pid2,os.getpid(),os.getppid()