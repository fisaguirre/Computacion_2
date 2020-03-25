#!/usr/bin/python3

#si no uso la version 3 no funciona para saldo
import threading
import time
import random

list = []
sem1 = threading.Semaphore(20)
sem2 = threading.Semaphore(0)

def transifere(cuanto):
    for i in range(cuanto):
        sem1.acquire()
        print ("agregando elmento a la lista: ",list)
        time.sleep(random.randrange(0,10)/100)
        list.append(i)
        print ("se agrego el elemento : ",i)
        print ("la lista quedo: ", list)
        sem2.release()

        

def consulta(cuanto):
    for i in range(cuanto):
        sem2.acquire()
        print ("sacando elemento de la lista", list)
        time.sleep(random.randrange(0,10)/100)
        num = list.pop()
        print ("se saco el elemento: ",num)
        print ("la lista quedo: ",list)
        sem1.release()
        


t1 = threading.Thread(name="h1", target=transifere, args=(200,))
t2 = threading.Thread(target=consulta, args=(200,))
t1.start()
t2.start()
t1.join()
t2.join()
