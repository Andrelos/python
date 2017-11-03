#!/usr/bin/env python

# -*- coding: utf-8 -*-


f = open('archivo.txt')
print f.read()
f.close()

#debo utilizar el modo para abrirlo segun que es lo que quiero hacer.

#modo write
f = open('archivo.txt','w') 
f.write('asi lo sobreescribo')
f.close()


#modo append
f = open('archivo.txt','a') 
f.write('asi lo sobreescribo1')
f.close()
