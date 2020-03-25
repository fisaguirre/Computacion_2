#!/usr/bin/python

from multiprocessing import Process
from multiprocessing import Queue



def funcion(numbers,q):
    for n in numbers:
        q.put(n*n)

if __name__ == '__main__':
    numbers = [2,4,6]
    q = Queue()
    p = Process(target=funcion, args=(numbers,q))
    
    p.start()
    p.join()

    while q.empty() is False:
        print 'la cola nos queda: ' , q.get()
