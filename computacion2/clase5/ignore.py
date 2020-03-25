#!/usr/bin/python

import os
from signal import *

def holaMundo(signalNumber, interruptedStackFrame):
    print("\n\nSignal number " + str(signalNumber) + " was ignored...")
    print(interruptedStackFrame)

signal(4, holaMundo)

print("Process ID: ", str(os.getpid()))
input("Esperando entrada")