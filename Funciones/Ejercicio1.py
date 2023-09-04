lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def AgregarNumeros():
    numero = int(input("Ingresa un número a la lista: "))
    lista.append(numero)
    print(lista)

AgregarNumeros()

def PareImpar():
    listaPar = []
    listaImpar = []
    for numero in lista:
        if numero % 2 == 0:
            listaPar.append(numero)
        else:
            listaImpar.append(numero)
    
    print("Números pares: ",listaPar)
    print("Números impares: ",listaImpar)

PareImpar()