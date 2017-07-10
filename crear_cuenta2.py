#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter
from tkinter import messagebox, Menu
from prueva_sqlite3 import DataBase,Read, ReadEntrar
from validate_email_address import validate_email
import sys
import os



def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

def close_and_open():

	VentanaEntrar.destroy()	
	crear_cuenta.crearcuenta()

class crear_cuenta:	


	def crearcuenta():


		def close_and_open1():

			dialog_title = 'Cuidado!'
			dialog_text = 'Estas seguro de salir?, todos tus datos se perderan!!!'

			answer = messagebox.askquestion(dialog_title, dialog_text)

			if answer == 'yes':

				VentanaPrincipal.destroy()

				restart_program()
			    
			else:  # 'no'

				print("click no")
			    


		##############################################################################################################################


		VentanaPrincipal = tkinter.Tk()

		VentanaPrincipal.focus_force()

		VentanaPrincipal.title("Crear Cuenta")

		VentanaPrincipal.geometry("800x600")

		VentanaPrincipal.config(bg="#e3f2fd")


		##############################################################################################################################

		menu_bar = Menu(VentanaPrincipal)
		file_menu = Menu(menu_bar, tearoff=0)

		file_menu.add_command(label="Cerrar!", command=VentanaPrincipal.destroy)
		file_menu.add_command(label="Ya tengo una Cuenta", command=close_and_open1)

		menu_bar.add_cascade(label="INICIO", menu=file_menu)

		VentanaPrincipal.config(menu=menu_bar)


		##############################################################################################################################

		def ventana_con_texto(texto, color):	
		    ventana = tkinter.Tk()
		    ventana.title("MySql")
		    ventana.geometry("300x200")
		    ventana.configure(background="#90a4ae")
		    texto = tkinter.Label(ventana, text=texto, bg=color)
		    texto.pack()
		    ventana.mainloop()

		def infoget():
			UserE = EntryUsername.get()
			PassE = EntryPassword.get()
			EmailE = EntryEmail.get()		
			Email2E = EntryEmail2.get()
			EmailValidation = validate_email(Email2E)
			UserValidation = Read.read_from_db_user(UserE)

			
			if Email2E==EmailE and EmailValidation==True and UserValidation==True and PassE != None:
				DataBase.Create(UserE, PassE, EmailE)
				ventana_con_texto("Tu cuenta ha sido creada exitosamente!", "#76ff03")


			elif Email2E!=EmailE:
				ventana_con_texto("Tus Emails no coinciden", "#b71c1c")

			elif EmailValidation==False:
				ventana_con_texto("Por favor escribe un Email Valido", "#b71c1c")

			elif UserValidation==False:
				ventana_con_texto("Usuario Existente", "#b71c1c")

			else:
				ventana_con_texto("Ha ocurrido un Error, revisa todos tus datos", "#b71c1c")





		##############################################################################################################################

		Username = tkinter.Label(text="Nombre de Usuario", bg = "#e3f2fd",)
		EntryUsername= tkinter.Entry(VentanaPrincipal)
		Username.pack()
		EntryUsername.pack()


		Password = tkinter.Label(text="Contrasena", bg = "#e3f2fd")
		EntryPassword= tkinter.Entry(VentanaPrincipal, show="*")
		Password.pack()
		EntryPassword.pack()

		Email = tkinter.Label(text="Email", bg = "#e3f2fd")
		EntryEmail= tkinter.Entry(VentanaPrincipal)
		Email.pack()
		EntryEmail.pack()

		Email2 = tkinter.Label(text="Repite tu Email", bg = "#e3f2fd")
		EntryEmail2= tkinter.Entry(VentanaPrincipal)
		Email2.pack()
		EntryEmail2.pack()


		# Creando la instancia del Boton


		BotonEntrar = tkinter.Button(fg="#a1dbcd", bg="#383a39", text="Crear Cuenta", command=infoget)
		BotonCerrar = tkinter.Button(fg="#a1dbcd", bg="#383a39", text="Cerrar", command=VentanaPrincipal.destroy)	
		BotonEntrarCuenta = tkinter.Button(fg="#a1dbcd", bg="#383a39", text="Ya tengo una cuenta!", command=close_and_open1)
		BotonEntrar.pack()
		BotonCerrar.pack()
		BotonEntrarCuenta.pack()

		VentanaPrincipal.mainloop()



#####################################################################################################################################################################
#####################################################################################################################################################################
#########################################################CREANDO LA VENTANA PRINCIPAL################################################################################
#####################################################################################################################################################################
#####################################################################################################################################################################



VentanaEntrar = tkinter.Tk()

VentanaEntrar.title("Iniciar Sesion")

VentanaEntrar.geometry("800x600")

VentanaEntrar.config(bg="#e3f2fd")

####################################################Creando Menu##########################################################################

menu_bar = Menu(VentanaEntrar)
file_menu = Menu(menu_bar, tearoff=0)

file_menu.add_command(label="Cerrar!", command=VentanaEntrar.destroy)
file_menu.add_command(label="Crear Cuenta Nueva", command=close_and_open)
menu_bar.add_cascade(label="INICIO", menu=file_menu)

VentanaEntrar.config(menu=menu_bar)


##############################################################################################################################
def ventana_con_texto(texto, color):
    ventana = tkinter.Tk()
    ventana.title("MySql")
    ventana.geometry("300x200")
    ventana.configure(background="#90a4ae")
    texto = tkinter.Label(ventana, text=texto, bg=color)
    texto.pack()
    ventana.mainloop()

def infoget():
	UserE = EntryUsername.get()
	PassE = EntryPassword.get()
	UserValidation = ReadEntrar.entrar(UserE, PassE)

	print (PassE)

	if UserValidation == True:

		ventana_con_texto("Estas Conectado!", "#76ff03")	

	else:

		ventana_con_texto("Ha ocurrido un Error, revisa todos tus datos", "#b71c1c")


Username = tkinter.Label(text="Nombre de Usuario", bg = "#e3f2fd",)
EntryUsername= tkinter.Entry(VentanaEntrar)
Username.pack()
EntryUsername.pack()

Password = tkinter.Label(text="Contrasena", bg = "#e3f2fd")
EntryPassword= tkinter.Entry(VentanaEntrar, show="*")
Password.pack()
EntryPassword.pack()


	
BotonEntrar = tkinter.Button(fg="#a1dbcd", bg="#383a39", text="Entrar", command=infoget)
BotonEntrar.pack()

BotonCerrar = tkinter.Button(fg="#a1dbcd", bg="#383a39", text="Cerrar", command=VentanaEntrar.destroy)
BotonCerrar.pack()

BotonCrearCuenta = tkinter.Button(fg="#a1dbcd", bg="#383a39", text="Crear Cuenta Nueva", command=close_and_open)
BotonCrearCuenta.pack()


VentanaEntrar.mainloop()



