#!/usr/bin/python3
from concurrent.futures import ProcessPoolExecutor
# from time import sleep
import os

def recibir_matriz(vector):
    print("recibir: ",vector)
    for respuesta_2 in vector:
        var = multiplicar_matriz(respuesta_2)
        return (var)    

def multiplicar_matriz(elemento):
    print("multiplicar: ",elemento)
    #return (os.getpid(), elemento*elemento)
    return (elemento*elemento)

matriz = [[3, 4, 5, 10, 6, 5],
          [10, 3, 7, 8, 3, 2],
          [6, 8, 2, 0, 8, 8],
          [4, 3, 9, 10, 10, 10],
          [4, 5, 7, 10, 8, 5],
          [10, 2, 6, 7, 2, 10]]

pool_2 = ProcessPoolExecutor(4)

for respuesta_1 in pool_2.map(recibir_matriz,matriz):
    print(respuesta_1)
    
