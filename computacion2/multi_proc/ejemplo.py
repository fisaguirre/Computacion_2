#!/usr/bin/python

from multiprocessing import Process
from multiprocessing import Queue
import os


def funcion(numbers,q):
    for n in numbers:
        q.put(n)
        print 'el numero es: ', n
        print 'proceso padre: ', os.getppid()
        print 'proceso hijo: ', os.getpid()


def process_2(numbers,q):
    for n in numbers:
        q.put(n)
    print 'proceso padre: ', os.getppid()
    print 'proceso hijo: ', os.getpid()



if __name__ == '__main__':
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    q = Queue()
    p = Process(target=funcion, args=(numbers,q))
    p2 = Process(target=funcion, args=(numbers,q))
    p.start()
    p2.start()
    p2.join()

    p.join()

    while q.empty() is False:
        print 'la cola nos queda: ' , q.get()
