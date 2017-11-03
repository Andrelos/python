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
		ventana_pr.configure(width=500, height=300)
		self.place(x=0 ,y=0, width=500, height=300)
		
		self.lista = tk.Listbox(self,borderwidth=3)
		self.lista.insert(0,"Item 1","Item 2","Item 3","Item 4")
		self.lista.place(x=10,y=10)
		
		self.boton = ttk.Button(self, text="Imprimir seleccion",command=self.imprimir)
		self.boton.place(x=20,y=200)
		
	def imprimir(self):
		print self.lista.get(self.lista.curselection())


##############################INSTANCIO LA CLASE Y LA EJECUTO#######################
ventana_pr = tk.Tk()
app = Aplicacion(ventana_pr)
app.mainloop()
