#!/usr/bin/python

def hacer_algo():
    print("algo")

if __name__ == "__main__":
    print("Ejecutando como programa principal")
    hacer_algo()

# __main__ es el nombre del ámbito en el que se ejecuta el código de nivel superior (el programa principal).
#si no corremos este programa como 'modulo.py', y lo importamos desde otro programa, __name__ va a tener como nombre el nombre del programa 'modulo.py'
#entonces no se ejecutara lo que hay dentro del if
#esto se usa solo si no se quiere que se ejecute cierta parte del programa


#https://es.stackoverflow.com/questions/32165/qu%C3%A9-es-if-name-main
