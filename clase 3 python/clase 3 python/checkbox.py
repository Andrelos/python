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


		self.checkbox_value = tk.BooleanVar(self)
		self.checkbox = ttk.Checkbutton(self,text="opcion",variable=self.checkbox_value,command=self.checkbox_clicked)
		self.checkbox.place(x=40,y=70)
		
	def checkbox_clicked(self):
		print(self.checkbox_value.get())

##############################INSTANCIO LA CLASE Y LA EJECUTO#######################
ventana_pr = tk.Tk()
app = Aplicacion(ventana_pr)
app.mainloop()
