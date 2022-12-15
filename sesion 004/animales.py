class Animal:
    def __init__(self):
        self.nombre = ""

    def informar_tipo(self):
        print(type(self))


gato = Animal()
gato.nombre = "misifu"
gato.informar_tipo()
print(gato.nombre)