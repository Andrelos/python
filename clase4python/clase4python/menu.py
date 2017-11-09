#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk

class Aplicacion(ttk.Frame):
	
	def __init__ (self,ventana_pr):
		ttk.Frame.__init__(self,ventana_pr)
		
		ventana_pr.title("Mi App python")
		self.place(x=0,y=0,width=600,height=600)
		
		self.barra_de_menu = tk.Menu(ventana_pr)
		
		#creamos las opciones 
		self.menu_archivo = tk.Menu(self.barra_de_menu, tearoff=0)
		self.menu_archivo.add_command(label="Nuevo",command=self.nuevo)
		
		self.menu_ayuda = tk.Menu(self.barra_de_menu, tearoff=0)
		self.menu_ayuda.add_command(label="Acerca de..",command=self.acerca_de)

		#las adherimos a la barra bajo un nombre global
		
		self.barra_de_menu.add_cascade(label="Archivo",menu=self.menu_archivo)
		self.barra_de_menu.add_cascade(label="Ayuda",menu=self.menu_ayuda)
		
		ventana_pr.configure(width=600,height=600,menu=self.barra_de_menu)
		
	def nuevo(self):
		print "Nuevo archivo."
	def acerca_de(self):
		print "Acerca de."

##############################INSTANCIO LA CLASE Y LA EJECUTO#######################
ventana_pr = tk.Tk()
app = Aplicacion(ventana_pr)
app.mainloop()
