#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

#creamos una variable para conectarnos
conn = sqlite3.connect("database.sqlite")

#diccioario para construir los datos a ingresar
clientes = {("Gustavo",36),("Oscar",45),("Pablo",55)}

cursor = conn.cursor()

#nombre y edad son variables del ciclo for
for nombre, edad in clientes:
	cursor.execute("INSERT INTO clientes VALUES (?,?)",(nombre, edad))


#esto guarda cambios
conn.commit()

#esto cierra conexion
conn.close()
