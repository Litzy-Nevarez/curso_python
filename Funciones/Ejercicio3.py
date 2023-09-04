def tipoNumero(num1, num2):

    if num1 > num2:
        return 1
    elif num2 > num1:
        return -1
    elif num1 == num2:
        return 0
    
num1 = int(input("Ingresa el primer número: "))
num2= int(input("Ingresa el segundo número: "))
print(tipoNumero(num1,num2))
     