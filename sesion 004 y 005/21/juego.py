from cartas import *

class Juego:
    def __init__(self):
        self.mazo = Mazo()
        self.jugador1 = Mazo(True)
        self.jugador2 = Mazo(True)

    def iniciar_juego(self):
        for i in range(2):
            self.jugador1.agregar_carta(self.mazo.entregar_carta())
            self.jugador2.agregar_carta(self.mazo.entregar_carta())

    def mostrar_juego(self, finalizado = False):
        print("Cartas jugador1")
        self.jugador1.mostrar_cartas(finalizado)
        print("Cartas jugador2")
        self.jugador2.mostrar_cartas(finalizado)
        if finalizado:
            print("Jugador1: %d y Jugador2: %d" 
              %(self.jugador1.valor_mazo(), self.jugador2.valor_mazo()))

    def valorar_juego(self):
        valor1 = self.jugador1.valor_mazo()
        valor2 = self.jugador2.valor_mazo()

        if valor1 > valor2 and valor1 <= 21:
            print("Gana el jugador1")
        elif valor2 > valor1 and valor2 <= 21:
            print("Gana el jugador2")
        elif valor1 < valor2 and valor2 > 21 and valor1 < 21:
            print("Gana el jugador1")
        elif valor2 < valor1 and valor1 > 21 and valor2 < 21:
            print("Gana el jugador2")
        else:
            print("Empate")

    def jugar(self):
        jugando = True
        self.iniciar_juego()

        print("Jugando", jugando)

        while jugando:
            self.mostrar_juego()
            if self.jugador1.valor_mazo() < 18:
                self.jugador1.agregar_carta(self.mazo.entregar_carta())
            if self.jugador2.valor_mazo() < 18:
                self.jugador2.agregar_carta(self.mazo.entregar_carta())
            if self.jugador1.valor_mazo() > 21 or self.jugador2.valor_mazo() > 21:
                Jugando = False
                break
            if self.jugador1.valor_mazo() >= 18 and self.jugador2.valor_mazo() >= 18:
                Jugando = False
                break
        
        self.mostrar_juego(True)
        self.valorar_juego()

if __name__ == '__main__':
    j = Juego()
    j.iniciar_juego()

    
    j.mostrar_juego(True)
    j.valorar_juego()