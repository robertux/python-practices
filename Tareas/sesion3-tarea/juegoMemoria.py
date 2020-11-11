import random
import sys

parejas = ['♙', '♙', '♘', '♘', '♔', '♔', '♖', '♖', '♕', '♕', '&', '&', '$', '$', '#', '#']
random.shuffle(parejas)
cuadricula = [parejas[0:4], parejas[4:8], parejas[8:12], parejas[12:16]]

parejasDescubiertas = []

def mostrarCuadricula(cuadricula):
	for i in range(4):
		for j in range(4):
			if ([i,j] in parejasDescubiertas):
				print('', cuadricula[i][j], '', end="")
			else:
				print(' _ ', end="")
		print("\n")

def coincide(cuadricula, pos1x, pos1y, pos2x, pos2y):
	print("pos1[",pos1x,"][",pos1y,"]: ", cuadricula[pos1x][pos1y], " pos2[",pos2x,"][",pos2y,"]: ", cuadricula[pos2x][pos2y])
	return cuadricula[pos1x][pos1y] == cuadricula[pos2x][pos2y]


while(len(parejasDescubiertas) < 16):
	mostrarCuadricula(cuadricula)
	pos1 = input("Ingrese posicion1 en formato (x,y): ")
	pos2 = input("Ingrese posicion2 en formato (x,y): ")

	if (len(pos1) == 0 or len(pos2) == 0):
		sys.exit()

	pos1x, pos1y = int(pos1[0]), int(pos1[2])
	pos2x, pos2y = int(pos2[0]), int(pos2[2])

	if (coincide(cuadricula, pos1x, pos1y, pos2x, pos2y)):
		parejasDescubiertas.append([pos1x,pos1y])
		parejasDescubiertas.append([pos2x,pos2y])
	else:
		print("No coinciden")
