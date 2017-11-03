#!/usr/bin/env python
# -*- coding: utf-8 -*-

#todas las clases son publicas.

class MiClase(object):
	def __init__(self):
		self._atributo_privado = 1
		
	def _funcion_privada(self):
		print self._atributo_privado
		
		
objeto = MiClase()

print objeto._atributo_privado

