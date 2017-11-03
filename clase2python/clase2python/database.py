#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

#creamos una variable para conectarnos
conn = sqlite3.connect("database.sqlite")

#creo un cursor
cursor = conn.cursor()

#ejecuto la consulta

cursor.execute("CREATE TABLE clientes (nombre TEXT,edad NUMERIC)")



#esto guarda cambios
conn.commit()

#esto cierra conexion
conn.close()


#http://sqlitebrowser.org/ este es el browser para el sqlite
