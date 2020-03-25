#!/usr/bin/python
from concurrent.futures import ProcessPoolExecutor
from time import sleep
import os

#Defino la funcion en la cual declaro una lista y un bucle para recorrerla e ir multiplicando
def cuadrado(elemento):
    return (os.getpid(), elemento*elemento)

#Completo el arreglo de mi lista
lista = [1,2,3,4,8,12,4,5]

pool = ProcessPoolExecutor(4)

#for respuesta in pool.map(cuadrado,lista):
#    print (respuesta)

