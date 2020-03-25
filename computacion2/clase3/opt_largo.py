#!/usr/bin/python

import sys
import getopt

print getopt.getopt(['--fernando','--isaguirre','agustin','--renato','isaguirre'],'',['fernando','isaguirre=','renato='])

#Para las opciones largas se usa --(que es como el - si fuera para un solo caracter), pero aca no hay que poner el -
#Si alguna opcion requiere de un argumento, en el tercer argumento debe ir precedido por un =(que serian los : si fuera de un solo caracter)