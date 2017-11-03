#!/usr/bin/env python
# -*- coding: utf-8 -*-
####################################################################################

import Tkinter as tk
import ttk 

####################################################################################

"""
pyinstaller crea un ejecutable
"""

##################################VENTANA PRINCIPAL#################################
#frame seria la ventana principal
class Aplicacion(ttk.Frame):
	
	def __init__(self,ventana_pr):
		ttk.Frame.__init__(self,ventana_pr)
		ventana_pr.title('Mi Aplicacion')
		ventana_pr.configure(width=300, height=300)
		self.place(x=0 ,y=0, width=300, height=300)
##############################BOTON#################################################		
		self.boton = ttk.Button(self,text="Hola", command=self.boton_presionado)
		self.boton.place(x=100,y=10)
##############################LABEL################################################		
		self.label = ttk.Label(self,text="hola mundo")
		self.label.pack()
		self.label.place(x=10,y=10)
##############################FUNCION###############################################		
	def boton_presionado(self):
		print "Presionado"
		
##############################INSTANCIO LA CLASE Y LA EJECUTO#######################
ventana_pr = tk.Tk()
app = Aplicacion(ventana_pr)
app.mainloop()
