#Ejercicio 1
cadena = "Te quiero solo como amigo"
tam = len(cadena)

#Imprima los dos primeros caracteres
print(cadena[0 : 2])
#Imprima los tres últimos caracteres
#print(cadena[-3], cadena[-2], cadena[-1])
print(cadena[-3 : ])
#Imprima dicha cadena cada dos caracteres. 
# Ej.: Si la cadena fuera “recta” debería imprimir 
# rca
print(cadena[ : : 2])
#Dicha cadena en sentido inverso.
print(cadena[ : : -1])
#Imprima la cadena en un sentido y en sentido inverso. 
print(cadena[0 : tam], cadena[ : : -1])
print(cadena + cadena[ : : -1])

#Ejercicio 2
palabra = "eparado"

cadena2 = "Este es el uso del metodo replace"
remplazar = cadena2.replace("e", "E")
print(remplazar)

print(palabra)
rem = palabra.replace("", ",")
print("S",rem)
