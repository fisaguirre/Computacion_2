#!/usr/bin/python

import sys
import getopt

#el modulo getopt es el analizador de opciones de linea de comandos por Unix
#Analiza una secuencia de argumentos, como sys.argv y devuelve una secuencia de pares (opción, argumento) y una secuencia de argumentos no opcionales.
#getopt toma tres argumentos

#El primer argumento es la secuencia de argumentos a analizar. Esto generalmente viene de sys.argv [1:] (ignorando el nombre del programa en sys.arg [0]).
#El segundo argumento es la cadena de definición de opción para las opciones de un solo carácter. Si una de las opciones requiere un argumento, su letra va seguida de dos puntos.
#El tercer argumento, si se usa, debe ser una secuencia de los nombres de opciones de estilo largo. Las opciones de estilo largo pueden ser más que un solo carácter, como --noarg o --witharg. Los nombres de las opciones en la secuencia no deben incluir el prefijo -. Si alguna opción larga requiere un argumento, su nombre debe tener un sufijo de =.

L = False
H = False
V = 0
opc ,argus = getopt.getopt(sys.argv[1:],'lhv:j')
#[inicio:fin(sin incluir):salto]
for o in opc:
    if o[0] == "-l":
        L = True
    elif o[0] == "-h":
        H = True
    elif o[0] == "-v":
        V = int (o[1])
        

print "L ", L
print "H ", H
print "V ", V
print "argus" , argus
print opc