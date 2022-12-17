from cronometro2 import *
from time import sleep

c = Cronometro()

for i in range(10000):
    c.avanzar()
    print(c.ver_tiempo())
    sleep(0.1)