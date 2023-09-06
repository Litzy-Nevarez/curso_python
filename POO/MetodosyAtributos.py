class FabricaTelefono():
    marca = "Huawei"
    color = "Negro"
    memoriaRam = 32
    almacenamiento = 128

    def llamar(self, mensaje):
        return mensaje
    
    def escucharMusica(self):
        print("Estas escuchando Música")

telefono = FabricaTelefono()
telefono.marca
telefono.color
telefono.memoriaRam
telefono.almacenamiento

print(telefono.llamar("Hola, con quién hablo?"))
print(telefono.escucharMusica())