#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import time
import datetime
import random


Base_de_datos = 'database12.db'

tabla = 'renatomoor123'



class DataBase:

	def Create(UserE, PassE, EmailE):

		print("Entraste a Create def")

		conn = sqlite3.connect(Base_de_datos)
		c = conn.cursor()
		print("Conectado")

		c.execute("CREATE TABLE IF NOT EXISTS "+tabla+"(unix REAL, datestamp TEXT, user TEXT, passw REAL, email TEXT)")
		conn.commit()

		print("Creaste tabla si no existia")
		unix = time.time()
		date = str(datetime.datetime.fromtimestamp(unix).strftime('%d-%m-%Y %H: %M: %S '))
		user = UserE
		passw = PassE
		email = EmailE

		print("Diste todos los valores a las variables")

		c.execute ("INSERT INTO "+tabla+"(unix, datestamp, user, passw, email) VALUES (?, ?, ?, ?, ?)",
		(unix, date, user, passw, email))

		print("inrodujiste los valores a la tabla")

		conn.commit()
		c.close
		conn.close()

		print("Cerraste la connetion")
		print ("creaste tu usuario!")

		return



class Read:

	def read_from_db_user(UserE):

		conn = sqlite3.connect(Base_de_datos)
		c = conn.cursor()
		c.execute("CREATE TABLE IF NOT EXISTS "+tabla+"(unix REAL, datestamp TEXT, user TEXT, passw REAL, email TEXT)")
		c.execute("SELECT user FROM "+tabla+" WHERE "+tabla+".user = '{}'" .format(UserE))

		data = c.fetchone()

		if data == None:
			conn.commit()
			c.close
			conn.close()
			print("Usuario Disponible")
			return True

		else:
			print("Usuario NO!!! Disponible")			
			return False


class ReadEntrar:

	def entrar(UserE, PassE):
		conn = sqlite3.connect(Base_de_datos)
		c = conn.cursor()

		c.execute("SELECT user FROM "+tabla+" WHERE "+tabla+".user = '{}'" .format(UserE))

		datauser = c.fetchone()

		c.execute("SELECT passw FROM "+tabla+" WHERE "+tabla+".passw = '{}'" .format(PassE))

		datapass = c.fetchone()

		print(datapass)

		print(datauser)

		if datauser == None or datapass == None:

			return False

		else:

			return True

		
    	






