class Calculadora:

    def __init__(self, v1 = 0, v2 = 0):
        self.valor1 = v1
        self.valor2 = v2
        self.resultado = 0
        self.operador = ""

    def suma(self):
        self.operador = " + "
        self.resultado = self.valor1 + self.valor2

    def resta(self):
        self.operador = " - "
        self.resultado = self.valor1 - self.valor2

    def producto(self):
        self.operador = " * "
        self.resultado = self.valor1 * self.valor2

    def division(self):
        self.operador = " / "
        self.resultado = self.valor1 // self.valor2

    def respuesta(self):
        return "%d %s %d = %d" %(self.valor1, self.operador,
                                 self.valor2, self.resultado)