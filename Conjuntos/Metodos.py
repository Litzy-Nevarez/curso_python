conjunto = {1, 1, 2, 3, 3, 4, 4, 5} #solo muestra los unicos valores

print(conjunto)

#añadir
conjunto.add(20)
print(conjunto)

#elimina un valor
conjunto.remove(1)
print(conjunto)

#pop eliminar cualquier alazar
conjunto.pop()
print(conjunto)

#añade elementos iterables
conjunto.update([1, 2, 3])
print(conjunto)

#conjunto vacio
conjunto.clear()
print(conjunto)