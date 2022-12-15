from banda import *

i = Banda([Guitarra(), Bajo(), Tiple(), Flauta(), Piano()])
i.armar_banda(['Alejandro', 'Miguel', 'Juan', 'Maria'])
i.presentar()
i.afinar()
i.tocar()