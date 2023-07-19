lista = [5, 4, 1, 2, 3, 5, 5]
print(lista)

#agregar
lista.append(6)
print(lista)
#lista.append("Litzy")
print(lista)
#lista.insert(2, 2.5)#posicion, valor
print(lista)

#cuenta la cantidad de veces de un elemento
print(lista.count(5))

#buscar en que posicion esta el elemento
print(lista.index(4))

#ordena la lista ascendente
lista.sort()
print(lista)
lista.reverse() #descendente
print(lista)
