#!/usr/bin/python

#!/usr/bin/python

import os
import sys
import argparse
import time
from getopt import getopt
from multiprocessing import Process
from multiprocessing import Queue

def funcion1():
    time.sleep(4)
    print "hijo1" , os.getpid(), os.getppid()

def funcion2():
    leido = q.get()
    print 'los datos son: ', leido
    print "hijo2", os.getpid(), os.getppid()
    leido = q.get()
    print 'otros son: ',leido

def funcion3(q):
    datos = [1,2,3,4,5,6,7,8,9,0]
    datos_2 = [10,11,12,13,14,15]
    q.put(datos)
    q.put(datos_2)

q = Queue()
process_1 = Process(target=funcion1,args=())
process_2 = Process(target=funcion2,args=())
process_3 = Process(target=funcion3,args=(q,))


process_1.start()
process_2.start()
process_3.start()


print 'terminaron ls hijos'

process_1.join()
process_2.join()
process_3.join()