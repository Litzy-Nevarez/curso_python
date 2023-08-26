def make_list(number):
    names = []
    for item in number:
        names.append(input("Tu nombre"))
    print(names)

number = int(input("numero"))
names = make_list(number)

for name in names:
    if name[i] == "A":
        print("name ",name, " empieza con A")