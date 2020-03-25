#!/usr/bin/python3

import threading
import time
import random

list = []
cond_1 = threading.Condition()


def produce(cuanto):
    for i in range(cuanto):
        print ("agregando elmento a la lista: ",list)
        time.sleep(random.randrange(0,10)/100)
        list.append(i)
        print ("se agrego el elemento : ",i)
        print ("la lista quedo: ", list)
    cond_1.re()

        

def cons(cuanto):
    cond_1.wait()
    for i in range(cuanto):
        print ("sacando elemento de la lista", list)
        time.sleep(random.randrange(0,10)/100)
        num = list.pop()
        print ("se saco el elemento: ",num)
        print ("la lista quedo: ",list)
    
        


t1 = threading.Thread(name="h1", target=produce, args=(5,))
t2 = threading.Thread(target=cons, args=(5,))
t1.start()
t2.start()
t1.join()
t2.join()
