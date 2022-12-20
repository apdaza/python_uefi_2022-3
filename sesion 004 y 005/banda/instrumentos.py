class Instrumento:
    def presentar(self):
        return(str(type(self)).split('.')[1][:-2])

    def afinar(self):
        pass

    def tocar(self):
        pass

class Guitarra(Instrumento):
    def afinar(self):
        return "Afinando Guitarra"

    def tocar(self):
        return "Tocando Guitarra"

class Bajo(Instrumento):
    def afinar(self):
        return "Afinando Bajo"

    def tocar(self):
        return "Tocando Bajo"

class Tiple(Instrumento):
    def afinar(self):
        return "Afinando Tiple"

    def tocar(self):
        return "Tocando Tiple"

class Flauta(Instrumento):
    def tocar(self):
        return "Tocando Flauta"

class Piano(Instrumento):
    def afinar(self):
        return "Afinando Piano"

    def tocar(self):
        return "Tocando Piano"