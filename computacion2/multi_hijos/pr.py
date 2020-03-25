#!/usr/bin/python

import sys
import getopt
import os
import time

print 'proceso padre: ',os.getpid(),os.getppid()
print format(os.getpid())
def child(id, sleepTime):
    print "I'm P"+str(id)
    print 'soy el hijo: ',os.getpid(), os.getppid()
    time.sleep(sleepTime)
    os._exit(0)
p1=os.fork()
if (p1==0):
    child(1,3)    #P1 sleeps for 3 seconds
p2=os.fork()
if (p2==0):
    child(2,5)   #P2 sleeps for 5 seconds
if (p1>0 and p2>0):
    os.waitpid(p1,0)   #Waiting for child 1
    os.waitpid(p2,0) #Waiting for child2
    print "I am the main process, the two processes are done"   #Printed after approx 5 seconds