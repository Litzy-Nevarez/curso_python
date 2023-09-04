
while True:

    try:
        edad = int(input("Ingrese su edad: "))
        print("Tu edad es: ",edad)
        break

    except ValueError:
        print("Ingresaste un valor erroneo")

    finally:
        print("La ejecución ha finalizado")