print("Promedio de un Alumno(a)")

p1 = float(input("Ingrese calificación de P1:"))
p2 = float(input("Ingrese calificación de P2:"))
p3 = float(input("Ingrese calificación de P3:"))
ep = float(input("Ingrese calificación del Examen Parcial:"))
ef = float(input("Ingrese calificación del Examen Final:"))

pp = (p1+p2+p3)/3
prom = (pp + (2*ep) + (3*ef))/6

print("Promedio de Práctcia:",pp, "Promedio Final:",prom)