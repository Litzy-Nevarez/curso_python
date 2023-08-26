'''a = list(map(int, input().split()))

b = []
i = 0

while i < len(a):
    if a[i] == 2 or a[i] == 3:
        b.append(a[i])
        a[i] = 0
    else:
        i += 1
print("A =", a)
print(len(b))

from time import *

start_time = time()
phrase = input("Escribe una reseña: ")
end_time = time()

total_time = end_time - start_time
symbols = len(phrase)
print("Velocidad de tipeo: ", symbols/total_time*60)

a = 5.4
b = 3
c = int(a//1) * b
print(c)


ingreso = int(input("Ingresa tu promedio mensual"))
num_horas = int(input("Ingresa tus horas trabajadas:"))

bono = (ingreso) * 0.01 * num_horas

print("Ingreso promedio mensual\n>>>",ingreso, "\nNumero de horas trabajadas en fines de semana:\n>>>",num_horas,"\nTamaño de bono:",bono)

categoria = input("Ingresa la categoría: ")
precio = int(input("Ingresa el precio del producto: "))

if categoria == "productos horneados":
    descuento = 0.3 * precio
    print("Descuento de 30%. Por pagar: ",(precio-descuento))
else:
    if categoria == "productos láscteos":
        descuento = 0.1 * precio
        print("Descuento de 10%. Por pagar: ",(precio-descuento))

#Escribe la función perimeter() para calcular el perímetro
def calcularPerimetro(lado1, lado2):
    perimetro = 2 * (lado1 + lado2)
    return perimetro
 
#Escribe la función area() para calcular el área
def calcularArea(lado1, lado2):
    area = lado1 * lado2
    return area

a = int(input("Ingresa el primer lado del rectángulo: "))
b = int(input("Ingresa el segundo lado del rectángulo: "))

print(calcularPerimetro(a,b))
print(calcularArea(a,b))'''

staff = {
    'Juan': {
        'cargo': 'marketing',
        'desempeño': 71
    },
    'Sofia': {
        'cargo': 'marketing',
        'desempeño': 65
    },
    'Andres': {
        'cargo': 'marketing',
        'desempeño': 49
    },
    'Romina': {
        'cargo': 'marketing',
        'desempeño': 53
    }
}

def identificar_y_eliminar_bajo_desempenio(staff_dict):
    trabajadores_bajos = []
    trabajadores_altos = []

    for trabajador, detalles in staff_dict.items():
        desempenio = detalles['desempeño']
        if desempenio < 50:
            print("Se recomienda despedir al trabajador", trabajador)
            trabajadores_bajos.append(trabajador)
        else:
            trabajadores_altos.append(trabajador)

    for trabajador_bajo in trabajadores_bajos:
        del staff_dict[trabajador_bajo]

    mostrar_trabajadores_alto = '\n'.join(map(str, trabajadores_altos))
    print("Trabajadores de alto desempeño:")
    print(mostrar_trabajadores_alto)

identificar_y_eliminar_bajo_desempenio(staff)

