#!/usr/bin/python

class Terrestre:
    def desplazar(self):
        print "el animal anda"

class Acuatico:
    def desplazar(self):
        print "el animal nada"

class Cocodrilo(Terrestre, Acuatico):
    pass

c = Cocodrilo()
c.desplazar()