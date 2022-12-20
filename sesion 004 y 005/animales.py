from random import choice

class Animal:
    def __init__(self):
        self.nombre = ""

    def informar_tipo(self):
        print(type(self))

    def comunicar(self):
        pass

class Gato(Animal):
    def comunicar(self):
        print("miauuuu")

class Perro(Animal):
    def comunicar(self):
        print("guau")

class Cacatua(Animal):
    def comunicar(self):
        print("pia-rua")

class Boa(Animal):
    def comunicar(self):
        print("ssssssss")

class Jirafa(Animal):
    pass

class Mixto(Perro, Boa):
    pass

class TiendaMascotas:
    def __init__(self):
        self.animal = None
        self.animales = [Gato(), Perro(), Cacatua(), Boa(), Jirafa(), Mixto()]

    def seleccionar_animal(self):
        self.animal = choice(self.animales)

if __name__ == "__main__":
    t = TiendaMascotas()
    t.seleccionar_animal()
    t.animal.informar_tipo()
    t.animal.nombre = choice(['misi','laika','max','perry'])
    print(t.animal.nombre)
    t.animal.comunicar()