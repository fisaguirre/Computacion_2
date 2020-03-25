#!/usr/bin/python3

#si no uso la version 3 no funciona para saldo
import threading
import time


saldo = 1000
sem = threading.Lock()
sem.acquire()

sem2 = threading.Lock()
sem2.acquire()

def transifere1(cuanto):
    global saldo
    saldo = saldo + cuanto
    
    sem.release()
    sem2.acquire()

    print ("el saldo final de transfiere1 es: ", saldo)
    time.sleep(5)
    print ("el saldo final de transfiere1 es: ", saldo)

#    print ("termino el hilo depo saldo: ", saldo)

def transifere2(cuanto):
    global saldo
    saldo = saldo + cuanto

    sem2.release()
    sem.acquire()

    print ("el saldo final de transfiere2 es: ",saldo)
    time.sleep(2)
    print ("el saldo final de transfiere2 es: ",saldo)

def extrae(cuanto):
    global saldo
    saldo = saldo - cuanto

    sem2.release()
    sem.acquire()

    print ("el saldo final de transfiere3 es: ",saldo)
    time.sleep(2)
    print ("el saldo final de transfiere3 es: ",saldo)


t1 = threading.Thread(name="h1", target=transifere1, args=(40000,))
t2 = threading.Thread(target=transifere2, args=(500,))
t23 = threading.Thread(target=extrae, args=(500,))

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

print ("valor saldo final", saldo)