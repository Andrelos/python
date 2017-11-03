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
############################ENTRADA DE DATOS########################################
		self.entry = ttk.Entry(self)
		self.entry.place(x=10,y=10)
####################################################################################		
		self.boton = ttk.Button(self, text="Imprimir texto", command=self.imprimir_texto)
		self.boton.place(x=10,y=50)
####################################################################################		
		self.boton2 = ttk.Button(self, text="Borrar texto", command=self.borrar_texto)
		self.boton2.place(x=100,y=50)
####################################################################################
		self.boton3 = ttk.Button(self, text="Agregar texto",command=self.agregar_texto)
		self.boton3.place(x=200,y=50)
####################################################################################				
	def imprimir_texto(self):
		print self.entry.get()
		
	def borrar_texto(self):
		self.entry.delete(0,tk.END)
	
	def agregar_texto(self):
		self.entry.insert(0,"texto")
		
		
##############################INSTANCIO LA CLASE Y LA EJECUTO#######################
ventana_pr = tk.Tk()
app = Aplicacion(ventana_pr)
app.mainloop()
