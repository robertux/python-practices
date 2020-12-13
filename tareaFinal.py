#!/usr/bin/python
import re

class Empleado:

	def __init__(self, dui, nit, sueldo, tiempo_trabajo):
		self.dui = dui
		self.nit = nit
		self.sueldo = sueldo
		self.tiempo_trabajo = tiempo_trabajo #en años
		self.aguinaldo = self.calcular_aguinaldo()

	def datos_validos(self):
		if (not re.match("\d{9}", self.dui)):
			print("DUI debe ser un valor numérico de 9 dígitos: ", self.dui)
			return False

		if (not re.match("\d{14}", self.nit)):
			print("NIT debe ser un valor numérico de 14 dígitos: ", self.nit)
			return False

		if (self.sueldo <= 0.00):
			print("Sueldo debe ser un valor positivo: ", self.sueldo)
			return False

		if (self.tiempo_trabajo < 0):
			print("Los anios de trabajo debe ser un valor positivo: ", self.tiempo_trabajo)
			return False

		return True

	def to_string(self):
		print(f'Empleado [dui: {self.dui[:8]}-{self.dui[8]}, nit: {self.nit[:4]}-{self.nit[4:10]}-{nit[10:13]}-{nit[13]}, sueldo: ${self.sueldo}, años trabajo: {self.tiempo_trabajo}, aguinaldo: {self.aguinaldo}]')

	def calcular_aguinaldo(self):
		if (self.datos_validos()):
			dias = 0
			if (self.tiempo_trabajo >= 1 and self.tiempo_trabajo <= 3):
				dias = 15
			if (self.tiempo_trabajo >= 4 and self.tiempo_trabajo <= 10):
				dias = 19
			if (self.tiempo_trabajo > 10):
				dias = 21

			return (self.sueldo / 30 * dias)
		else:
			return 0.0


dui = input("Ingrese el DUI del empleado (sin guiones): ")
nit = input("Ingrese el NIT del empleado (sin guiones): ")
sueldo = float(input("Ingrese el sueldo del empleado: "))
anios = int(input("Ingrese los años de trabajo: "))

emp = Empleado(dui, nit, sueldo, anios)
if (emp.datos_validos()):
	print(emp.to_string())
else:
	print("Datos inválidos")
