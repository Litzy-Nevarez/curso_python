num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))

for i in range(num1, num2+1):
    if i % 2 == 0:
        continue
    print(i)