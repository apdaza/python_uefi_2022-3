from unidad_tiempo import UnidadTiempo

class Cronometro:
    def __init__(self):
        self.hora = UnidadTiempo('Hora', 23)
        self.minuto = UnidadTiempo('Minuto', 59)
        self.segundo = UnidadTiempo('Segundo', 59)
        self.decima = UnidadTiempo("Decima", 9)

        self.parado = True

    def avanzar(self):
        self.decima.avanzar()
        if self.decima.valor == 0:
            self.segundo.avanzar()
            if self.segundo.valor == 0:
                self.minuto.avanzar()
                if self.minuto.valor == 0:
                    self.hora.avanzar()


    def retroceder(self):
        self.decima.retroceder()
        if self.decima.valor == self.decima.tope:
            self.segundo.retroceder()
            if self.segundo.valor == self.segundo.tope:
                self.minuto.retroceder()
                if self.minuto.valor == self.minuto.tope:
                    self.hora.retroceder()

    def borrar(self):
        self.decima.borrar()
        self.segundo.borrar()
        self.minuto.borrar()
        self.hora.borrar()

    def ver_tiempo(self):
        return "%s : %s : %s : %s" % (self.hora.ver_valor(),
                                 self.minuto.ver_valor(),
                                 self.segundo.ver_valor(),
                                 self.decima.ver_valor())

    def setear(self, valores):
        self.hora.setear(valores[0])
        self.minuto.setear(valores[1])
        self.segundo.setear(valores[2])
        self.decima.setear(valores[3])