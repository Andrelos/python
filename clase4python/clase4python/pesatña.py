#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk

####################################################################################
class Aplicacion(ttk.Frame):
	def __init__ (self,main_window):
		ttk.Frame.__init__(self)
		main_window.title("Panel de pestañas")
		

		
		#creamos panel
		self.notebook = ttk.Notebook(main_window)
		
		#creamos el contenido de cada una de las pestañas
		self.web_label = ttk.Label(self.notebook, text="Texto en la pestaña 1")
		self.forum_label = ttk.Label(self.notebook, text="texto en pesataña 2")
		
		self.notebook.add(self.web_label, text="Pestaña 1", padding=20)
		self.notebook.add(self.forum_label, text="Pestaña 2", padding=20)
		
		self.notebook.pack(padx=10,pady=10)
		self.pack()
	
	
##############################INSTANCIO LA CLASE Y LA EJECUTO#######################
main_window = tk.Tk()
app = Aplicacion(main_window)
app.mainloop()
