#!/usr/bin/python
import os

leido = 0
EOF = True

while EOF :
    leido = os.read(0,1000)
    if len(leido) < 1000:
        EOF = False

    
def reverse(leido):
    i = 0
    leido3 = ""
    cant = 0
    cant = cant + len(leido.strip())
    leido_final = ""
    for f in leido:
        if(leido[i]!= " "):
            leido3 = leido3+leido[i]
        if( (leido[i]== " ") or (i==cant) ):
            leido4=leido3[::-1]
            leido3=""
            leido_final = leido_final + leido4 + " "
            leido4 = ""
        i+=1
    os.write(1,leido_final + "\n")

reverse(leido)