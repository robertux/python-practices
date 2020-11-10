lista = [5,9,1,58,4,2.65,10.8]

lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

maximo = lista[0]
print(maximo)

lista.sort()
minimo = lista[0]
print(minimo)


minimo = min(lista)
print(minimo)

maximo = max(lista)
print(maximo)

longitud = len(lista)
print(longitud)

busqueda = 5 in lista
print(busqueda)

indice = lista.index(4)
print(indice)

cuenta = lista.count(9)
print(cuenta)
