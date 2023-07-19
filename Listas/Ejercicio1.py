'''En la siguiente lista, debes hacer un programa que 
muestre los valores al usuario, a su vez, debe pedir dos 
datos y esos que sean ingresados deben ser sustituidos 
en el primer y segundo lugar:
[20, 50, "Curso", 'Python', 3.14]'''

lista = [20, 50, "Curso", 'Python', 3.14]

print(lista)

valor1 = int(input("Ingresa un valor numerico: "))
valor2 = int(input("Ingresa otro valor numerico: "))

lista[0] = valor1
lista[1] = valor2

print(lista)