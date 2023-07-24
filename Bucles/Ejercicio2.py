'''Escribir un programa que pregunte al usuario su 
edad y muestre por pantalla todos los años que ha 
cumplido (desde 1 hasta su edad).'''

edad = int(input("Ingrese su edad: "))

i = 1
while i <= edad:
    print("Has cumplido: ", (i))
    i += 1

