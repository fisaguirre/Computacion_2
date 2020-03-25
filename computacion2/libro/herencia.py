#!/usr/bin/python

class Instrumento:
    def __init__(self, precio):
        self.precio = precio
    def tocar(self):
        print "Estamos tocando musica"
    def romper(self):
        print "Eso lo pagas tu"
        print "Son", self.precio, "$$$"

class Bateria(Instrumento):
    pass
class Guitarra(Instrumento):
    pass

b = Bateria(5)
b.romper()
