#!/usr/bin/python3

#si no uso la version 3 no funciona para saldo
import threading
import time


saldo = 1000
sem = threading.Lock()
sem.acquire()

def transifere(cuanto):
    global saldo
    for i in range(cuanto):
        saldo = saldo + 1
    sem.release()
#    print ("termino el hilo depo saldo: ", saldo)

def consulta():
    global saldo
    sem.acquire()

    print ("la consulta del saldo es: ",saldo)

t1 = threading.Thread(name="h1", target=transifere, args=(40000,))
t2 = threading.Thread(target=consulta)
t1.start()
t2.start()
t1.join()
t2.join()
print ("valor saldo final", saldo)