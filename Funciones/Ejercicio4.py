def calcularIVA():
    monto = float(input("Ingresa el valor del producto: "))
    iva = float(input("Ingresa el IVA: "))

    if iva != 0:
        if iva > 0:
            totalPagar = ((monto * iva) / 100) + monto
            return totalPagar
        else:
            return "El monto de IVA es negativo.No podemos avanzar"
    else:
        totalPagar = (monto * 0.21) + monto
        return totalPagar
    
print("El total de su monto es: ", calcularIVA())