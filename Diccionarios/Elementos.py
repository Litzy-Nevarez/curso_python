diccionario = {'Nombre' : 'Litzy', 'Apellido' : 'Nevarez', 'Estatura' : 1.60}

#solo mostrar las claves
print(diccionario.keys())
#muestra los valores
print(diccionario.values())
#quiero ver el valor de la clave estatura
print(diccionario['Estatura'])
#agregar nuevo
diccionario['Peso'] = "68 kg"
#modificar el valor
diccionario['Nombre'] = "Yulissa"

print(diccionario)
