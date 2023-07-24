diccionario = {1 : 2, 2 : 3, 3 : 4}
diccionario2 = {4 : 5, 6 : 7}

print(diccionario)

#elimina la clave asiganda
diccionario.pop(3)
print(diccionario)

#limpia el diccionario
diccionario.clear()
print(diccionario)

#devuelve el valor de la llave especificada
print(diccionario.get(2))

#agregar valores
diccionario.setdefault(4, 5)
print(diccionario)

#Unen los diccionarios (actualiza)
diccionario.update(diccionario2)
print(diccionario)

#saca una copia
diccionario.copy()
print(diccionario)