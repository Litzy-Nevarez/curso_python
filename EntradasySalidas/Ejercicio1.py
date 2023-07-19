'''Realizar un programa que haga el proceso de formula 
general para la resolución de ecuaciones, 
sabiendo que la formula general es la que está en 
la imagen, el usuario debe ingresar los valores 
de “a”, “b” y “c”, y el programa debe hacer 
el proceso para que al final muestre el mensaje: 
“La solución es: <solucion>”'''

import math

print("** Formula General **")

a = float(input("Ingresa el valor de a:"))
b = float(input("Ingresa el valor de b:"))
c = float(input("Ingresa el valor de c:"))

x1 = ((-b) + math.sqrt((b ** 2) - (4*a*c)))/(2*a)
x2 = ((-b) - math.sqrt((b ** 2) - (4*a*c)))/(2*a)

print("X1:", x1, "X2:", x2)