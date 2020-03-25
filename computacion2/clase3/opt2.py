#!/usr/bin/python

import sys
import getopt

print getopt.getopt(['-a','-fer','-s','-hval'],'af:sh:')

#El segundo argumento es la cadena de definición de opción para las opciones de un solo carácter. Si una de las opciones requiere un argumento, su letra va seguida de dos puntos.
