'''Crear un programa que permita al usuario elegir 
un candidato por el cual votar. Las posibilidades 
son: candidato A por el partido rojo, candidato B 
por el partido verde, 
candidato C por el partido azul. 
Según el candidato elegido (A, B ó C) 
se le debe imprimir el mensaje “Usted ha votado por 
el partido [color que corresponda al candidato elegido]”. 
Si el usuario ingresa una opción que no corresponde a 
ninguno de los candidatos disponibles, 
indicar “Opción errónea”.'''

candidato = input("Ingrese un candidato (A,B,C):")

if candidato.lower() == "a":
    print("Usted ha votado por el partido Rojo")
elif candidato.lower() == "b":
    print("Usted ha votado por el partido Verde")
elif candidato.lower() == "c":
    print("Usted ha votado por el partido Azul")
else:
    print("Opción erronea")