'''Escribe una lista que tenga los números de 1 al 10. 
Luego, debes hacer que los datos que están en las 
posiciones 4, 7 y 9 sean multiplicados por 2; 
por último, mostrar la lista nueva con los nuevos 
datos'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Lista Original: ", lista)

valor_posicion4 = lista[4]
valor_posicion7 = lista[7]
valor_posicion9 = lista[9]

nuevoValor4 = valor_posicion4 * 2
nuevoValor7 = valor_posicion7 * 2
nuevoValor9 = valor_posicion9 * 2

lista[4] = nuevoValor4
lista[7] = nuevoValor7
lista[9] = nuevoValor9

print("Nueva lista: ", lista)

lista[3] *= 2
