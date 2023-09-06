#class FabricaTelefono():
#    marca = "Sambung"

#    def ElaborarHuawei(self):
#        self.arca = "Huawei"

#telefono = FabricaTelefono()

#print(telefono.marca)

#print(telefono.ElaborarHuawei())

class FabricaTelefono():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

telefono = FabricaTelefono("Huawei", "Negro")
print(telefono.marca)
print(telefono.color)
    
