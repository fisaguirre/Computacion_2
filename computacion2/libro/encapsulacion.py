#!/usr/bin/python

class Fecha():
    def __init__(self):
        self.__dia = 1
        #con init instancia el objeto
        #y establezco como inicializacion al atributo dia el valor 1
    def getDia(self):
        print self.__dia
        #return self.__dia
    def setDia(self, dia):
        if dia > 0 and dia < 31:
            self.__dia = dia
        else:
            print "Error"


mi_fecha = Fecha()
mi_fecha.setDia(22)
mi_fecha.getDia()
