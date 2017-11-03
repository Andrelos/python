#!/usr/bin/env python
# -*- coding: utf-8 -*-

#nombre de la clase con MAYUSCULA y sin guiones, el object es necesario ponerlo en la version 2 de python y no en la 3
class MiClase(object):
	def __init__(self): 
		print "creaste una instancia de la clase"
		
mi_objeto = MiClase()

class MiClase(object):
	def __init__(self):
		self.a = 1
mi_objeto = MiClase()
print mi_objeto.a

#asi lo llamo desde afuera
mi_objeto.a += 1
print mi_objeto.a 
