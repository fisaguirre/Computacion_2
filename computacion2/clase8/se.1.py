#!/usr/bin/python3

#si no uso la version 3 no funciona para saldo
import threading
import time


saldo = 1000
mutex = threading.Lock()

def transifere(cuanto):
    global saldo
    for i in range(cuanto):
        mutex.acquire()
        saldo = saldo + 1
        mutex.release()
#    print ("termino el hilo depo saldo: ", saldo)

def consulta(cuanto):
    global saldo
    for i in range(cuanto):
        mutex.acquire()
        saldo = saldo -1
        mutex.release()

    print ("la consulta del saldo es: ",saldo)

t1 = threading.Thread(name="h1", target=transifere, args=(10000,))
t2 = threading.Thread(target=consulta, args=(10000,))
t1.start()
t2.start()
t1.join()
t2.join()
print ("valor saldo final", saldo)