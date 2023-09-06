class FabricaTelefono():

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        print("El objeto {} ha sido creado".format(self.marca))

    def __str__(self):
        return "El objeto es {}".format(self.marca)
    
    def __del__(self):
        print("El objeto {} ha sido destruido".format(self.marca))

telefono = FabricaTelefono("Nokia", "Negro")
print(telefono.marca)