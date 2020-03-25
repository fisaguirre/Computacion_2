#!/usr/bin/python
class Ejemplo:
    def publico(self):
        print "Publico"
    def __privado(self):
        print "Privado"

ej = Ejemplo()
ej.publico()
#ej.__privado()
#si descomento esto no puedo acceder al metodo privado
ej._Ejemplo__privado()
#con esta trampa puedo acceder al metodo privado