#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
	int([1,2,3])
except (ValueError,TypeError): #esto maneja errores de valor, por eso ValueError
	print "Eso no es un numero o no se puede convertir ese tipo de datos"


#esto era un diccionario
#d = {"a" : 1}
#print d["b"]


"""
si no hago try escapa del programa
"""

try:
	int("10")
except Exception:
	print "Ocurrio un error"
else:
	print "todo salio bien"
