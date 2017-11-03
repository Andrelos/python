#!/usr/bin/env python
# -*- coding: utf-8 -*-

#F8 compila
#F5 ejecuta


def fib(cantidad):
	#validamos el número
	if cantidad <=2:
		print "La cantidad debe ser mayor que 2"
		#terminamos la función
		return
	#iniciamos la variable a retornar
	ret = [0, 2]
	#agregar tantos elementos como fueron indicados por parametro
	while len(ret) < cantidad:
		ret.append(ret[-1] + ret[-2])
	print ret
	return ret
fib(12)

