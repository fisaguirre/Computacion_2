#!/usr/bin/python
from concurrent.futures import ProcessPoolExecutor
from time import sleep
import os

def recibir_matriz(dato):
    return (dato)

def multiplicar_matriz(elemento):
    return (os.getpid(), elemento*elemento)

matriz = [[3, 4, 5, 10, 6, 5],
          [10, 3, 7, 8, 3, 2],
          [6, 8, 2, 0, 8, 8],
          [4, 3, 9, 10, 10, 10],
          [4, 5, 7, 10, 8, 5],
          [10, 2, 6, 7, 2, 10]]


pool_1 = ProcessPoolExecutor(4)
pool_2 = ProcessPoolExecutor(4)

for respuesta_1 in matriz:
    vector = respuesta_1
    for respuesta_2 in pool_2.map()
    print("vector:")
    for respuesta_2 in pool_2.map(multiplicar_matriz, respuesta_1):
        print (respuesta_2)
