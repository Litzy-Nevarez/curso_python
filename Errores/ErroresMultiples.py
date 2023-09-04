
while True:

    try:
        num = int(input("Ingrese un número: "))
        resultado = 100/ num
        print(resultado)
        break

    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        