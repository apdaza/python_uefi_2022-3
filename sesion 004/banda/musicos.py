from instrumentos import *

class Musico:
    def __init__(self, nombre, instrumento):
       self.nombre = nombre
       self.instrumento = instrumento 

    def presentar(self):
        print("mi nombre es %s y toco el instrmento %s" 
             % (self.nombre, self.instrumento.presentar()))

    def afinar(self):
        print(self.instrumento.afinar())

    def tocar(self):
        print(self.instrumento.tocar())