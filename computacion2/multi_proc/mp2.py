#!/usr/bin/python

from multiprocessing import Process

result = []
tupla = [1,2]
tupla_2 = [3,4,5,6,7,8,9]

def funcion(number):
    global result
    for n in number:
        result.append(n*n)
        #append agrega elementos al final de la lista result(solo agrega, no reemplaza)

    print 'la lista result es: ', str(result)

def agregar_tupla():
    result.append(1)
    result.append(tupla)

    print 'con la tupla queda: ', str(result)

def agregar_elementos_tupla():
    tupla.extend(tupla_2)
    
    print 'con la tupla2 queda: ', str(tupla)



if __name__ == '__main__':
    numbers = [2,4,6]
    p = Process(target=funcion, args=(numbers,))
    #en el libro a los parametros tambien le dicen argumentos
    p2 = Process(target=agregar_tupla)
    p3 = Process(target=agregar_elementos_tupla)
    p.start()
    p.join()

    p2.start()
    p2.join()
    #supuestamente join hace que se termine de ejecutar el proceso hijo y despues continua el proceso padre
    #lo que hace es unir al proceso de nuevo(como en fork, que lo que hace es dividir al proceso para luego unirse y ser uno solo)
    p3.start()
    p3.join()

    print 'outside process: ', str(result)