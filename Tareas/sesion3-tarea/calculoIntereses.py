
interes = float(input("Ingrese el porcentaje de interés: "))
monto = float(input("Ingrese el monto total a solicitar: "))
meses = int(input("Ingrese la cantidad de meses para realizar los pagos: "))

acumulado = monto / meses
pagos = []

for i in range(meses):
	acumulado += acumulado * interes / 100
	pagos.append(acumulado)

print("incremento de capital e intereses: ", pagos)
