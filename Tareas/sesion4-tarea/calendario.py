import datetime

meses = ('Enero', 'Febrero', 'Mazo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
diasEnMes = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
diasSemana = ('Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sab', 'Dom')
calendario = []


anio = int(input("Ingrese el año a consultar: "))
mes = int(input("Ingrese el mes a consultar: "))

fecha = datetime.date(anio, mes, 1)
primerDiaMes = fecha.weekday()

print("---------------------------------------------------")
print(meses[mes - 1])
print("---------------------------------------------------")

for dia in diasSemana:
	print(dia, end="\t")

print()
print("---------------------------------------------------")

for i in range(primerDiaMes):
	print("", end="\t")

for dia in range(diasEnMes[mes - 1]):
	print(dia + 1, end="\t")

	if ((dia + primerDiaMes + 1) % 7 == 0):
		print()

print()
print("---------------------------------------------------")

