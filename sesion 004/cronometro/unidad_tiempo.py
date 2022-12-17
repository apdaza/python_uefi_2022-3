class UnidadTiempo:
    def __init__(self, nombre, tope=59):
        self.nombre = nombre
        self.valor = 0
        self.tope = tope

    def avanzar(self):
        if self.valor < self.tope:
            self.valor += 1
        else:
            self.valor = 0

    def retroceder(self):
        if self.valor > 0:
            self.valor -= 1
        else:
            self.valor = self.tope

    def borrar(self):
        self.valor = 0

    def ver_valor(self):
        return "{:02d}".format(self.valor)

