from unidad_tiempo import UnidadTiempo

class Cronometro:
    def __init__(self):
        self.unidades = [UnidadTiempo('Decima', 9),
                         UnidadTiempo('Segundo', 59),
                         UnidadTiempo('Minuto', 59),
                         UnidadTiempo("Hora", 23)]

        self.parado = True

    def avanzar(self):
        for u in self.unidades:
            u.avanzar()
            if u.valor != 0:
                break 


    def retroceder(self):
        for u in self.unidades:
            u.retroceder()
            if u.valor != u.tope:
                break

    def borrar(self):
        for u in self.unidades:
            u.borrar()

    def ver_tiempo(self):
        tiempo = ""
        for u in self.unidades[::-1]:
            tiempo += u.ver_valor() + " : "

        return tiempo[:-3]

    def setear(self, valores):
        elemento = -1
        for u in self.unidades:
            u.setear(valores[elemento])
            elemento -= 1

