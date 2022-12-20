from musicos import *
from random import choice

class Banda:
    def __init__(self, instrumentos):
        self.musicos = []
        self.instrumentos = instrumentos

    def presentar(self):
        for m in self.musicos:
            m.presentar()

    def afinar(self):
        for m in self.musicos:
            m.afinar()

    def tocar(self):
        for m in self.musicos:
            m.tocar()

    def armar_banda(self, nombres):
        for n in nombres:
            self.musicos.append(Musico(n, choice(self.instrumentos)))