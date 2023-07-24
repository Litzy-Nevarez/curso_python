'''Escribir una tupla que tenga las letras del 
alfabeto. Luego, debes pedir al usuario un número, 
el que haya ingresado, es la letra que debe imprimir 
el programa'''

alfabeto = "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "u", "v", "w", "x", "y", "z"

numero = int(input("Ingresa un número: "))

print("La letra es: ", alfabeto[numero - 1])