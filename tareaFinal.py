#!/usr/bin/python

class Empleado:

	def __init__(self, dui, nit, sueldo, tiempo_trabajo):
		self.dui = dui
		self.nit = nit
		self.sueldo = sueldo
		self.tiempo_trabajo = tiempo_trabajo #{"anios": 0, "meses": 0, "dias": 0}

	def datos_validos(self):
		if (len(self.dui) != 9):
			print("Longitud incorrecta de DUI: ", len(str(self.dui)))
			return False

		if (len(self.nit) != 14):
			print("Longitud incorrecta de NIT: ", len(str(self.nit)))
			return False

		if (self.sueldo <= 0.00):
			print("Sueldo debe ser un valor positivo: ", self.sueldo)
			return False

		if (self.tiempo_trabajo["anios"] < 0):
			print("Los anios de trabajo debe ser un valor positivo: ", self.tiempo_trabajo["anios"])
			return False

		if (self.tiempo_trabajo["meses"] < 0):
			print("Los meses de trabajo debe ser un valor positivo: ", self.tiempo_trabajo["meses"])
			return False

		if (self.tiempo_trabajo["dias"] < 0):
			print("Los dias de trabajo debe ser un valor positivo: ", self.tiempo_trabajo["dias"])
			return False

		return True

	def to_string(self):
		print(f'Empleado[dui: {self.dui[:8]}-{self.dui[8]}, nit: {self.nit[:4]}-{self.nit[4:10]}-{nit[10:13]}-{nit[13]}, sueldo: ${self.sueldo}, tiempo_trabajo: {self.tiempo_trabajo}]')

	def calcular_aguinaldo():
		if (not self.datos_validos()):
			return 0.00


dui = input("Ingrese el DUI del empleado (sin guiones): ")
nit = input("Ingrese el NIT del empleado (sin guiones): ")
sueldo = float(input("Ingrese el sueldo del empleado: "))
anios = int(input("Ingrese los años de trabajo: "))
meses = int(input("Ingrese los meses de trabajo: "))
dias = int(input("Ingrese los dias de trabajo: "))

emp = Empleado(dui, nit, sueldo, {"anios": anios, "meses": meses, "dias": dias})
if (emp.datos_validos()):
	print(emp.to_string())
else:
	print("Datos inválidos")
