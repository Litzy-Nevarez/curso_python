class A():
    def __init__(self):
        self.contador = 0

    def incrementar(self):
        self.contador += 1

    def cuenta(self):
        return self.contador
    
class B():
    def __init__(self):
        self.__contador = 0

    def incrementar(self):
        self.__contador += 1

    def cuenta(self):
        return self.__contador

a = A()
print(a.cuenta())
print(a.incrementar())