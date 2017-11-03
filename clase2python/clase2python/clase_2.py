#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Clase2(object):
	def __init__(self, a):
		self.a = a
	def imprimir_a(self):
		print self.a
	def imprime_suma(self, n):
		self.a +=n
		print "el resultado de la suma es: " + str(self.a)
		
objeto = Clase2(8)
objeto.imprime_suma(10)
