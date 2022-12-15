from banda import *
from random import choices, randint

instrumentos = choices([Guitarra(), Bajo(), Tiple(), Flauta(), Piano()], k=randint(1,5))
nombres = choices(['Alejandro', 'Miguel', 'Juan', 'Maria'], k=randint(1,4))
i = Banda(instrumentos)
i.armar_banda(nombres)
i.presentar()
i.afinar()
i.tocar()