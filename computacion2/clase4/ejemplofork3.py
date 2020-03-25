#!/usr/bin/python
#El par de caracteres #! indica al sistema operativo que dicho script se debe ejecutar utilizando el intérprete especificado a continuación
import os

print os.getpid()

os.execv("/bin/ps", ("/bin/ps","-f"))

#crear procesos hijo para que ejecute lo de arriba y el proceso padre espere a que termine el hijo y despues vea como termino