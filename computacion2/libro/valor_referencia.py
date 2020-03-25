#!/usr/bin/python

def f(x, y):
 x = x + 3
 y.append(23)
 print x, y
 #aca imprimira los valores modificados
x = 22
y = [22]
f(x, y)
print x, y
#aca imprimira el valor de x "22" porque al llamar a la funcion f, estoy pasando parametros por valor y no por referencia, entonces no se modifica la 
#variable global "x", solo se modifica dentro de la funcion f
#pero sobretodo, es porque los enteros en python son inmutables

#y append es un metodo de las listas que agrega un elemento a la lista
#las listas en python son mutables, por eso se agrega el elemento

#los valores inmutables se comportan como paso por valor, y los mutables como por referencia