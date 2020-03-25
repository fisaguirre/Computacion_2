#!/usr/bin/python

# IMPORT
import sys
import getopt
import os

# VARIABLES
pid = 0
sig = ""
P = False 
C = False
# GET ARGS
args = sys.argv[1:]
options, arguments = getopt.getopt(args, "p:s:h")

# PROCESS ARGS
for item in options:
    if item[0] == "-p":
        pid = int(item[1])
        P = True
    elif item[0] == "-s":
        sig = int(item[1])
        C = True
    elif item[0] == "-h":
        print "Uso: ", sys.argv[0], " -p pid - s senial"
        os._exit(0)
if P == True and C == True:
    os.kill(pid, sig)
else:
    print "Uso: ", sys.argv[0], " -p pid - s senial"