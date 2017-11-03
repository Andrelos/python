#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ClaseA(object):
	def __init__(self):
		self.a = 1
		
	def mensaje(self):
		print "Mensaje 1"
		
		
class ClaseB(object):
	def __init__(self):
		self.a = 2
		
	def mensaje(self):
		print "Mensaje 2"
		
		

class ClaseC(ClaseA,ClaseB):
	#pass es para rellenar codigo, no quiero escribir nada pero no quiero que me tire un error
	pass
		

objetoC = ClaseC()
print objetoC.mensaje()


