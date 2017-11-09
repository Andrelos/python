#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk
import tkMessageBox as messagebox

class Aplicacion(ttk.Frame):
	def __init__ (self, ventana_pr):
		ttk.Frame.__init__(self, ventana_pr)
		
		self.texto_nombre = ttk.Entry(self)
		self.texto_nombre.place(x=10,y=10,width=200,height=25)
		
		self.boton_saludar = ttk.Button(self, text="Saludar!", command=self.saludar)
		self.boton_saludar.place(x=10,y=210)
		
		self.label_saludo = ttk.Label(self)
		self.label_saludo.place(x=10,y=40,width=140)
		
		self.lista_nombres = tk.Listbox(self)
		self.lista_nombres.place(x=10,y=60,width=280,height=130)
		
		self.place(x=0,y=0,width=300,height=300)

		ventana_pr.title("Lab 4")
		
		ventana_pr.configure(width=300,height=300)

		
		self.saludos = 0
		
		
		
		
		
	def saludar(self):
		print "hasta"
		if self.saludos == 5:
			messagebox.showerror(
				title="Error",
				message="Ya se emitieron 5 saludos"
				
			)
			return
		
		nombre = self.texto_nombre.get()
		
		
		
		if nombre:
			self.label_saludo.configure(
				text="Hola {}".format(nombre)
			)
			
			self.lista_nombres.insert(tk.END, nombre)
			self.texto_nombre.delete(0,tk.END)
			self.saludos+=1
		else:
			messagebox.showinfo(
				title="Campo vacio",
				message="No se ingreso ningun nombre"
			)	
		
ventana_pr = tk.Tk()
app = Aplicacion(ventana_pr)
bit = ventana_pr.iconbitmap('s.ico')
app.mainloop()
