from cronometro import *
from time import sleep

c = Cronometro()
c.setear([10, 20, 5, 3])

for i in range(10000):   
    c.retroceder()
    print(c.ver_tiempo())
    sleep(0.1)