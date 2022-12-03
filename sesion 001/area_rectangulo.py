from math import sqrt

punto1 = input("Ingrese el punto 1: ")
punto2 = input("Ingrese el punto 2: ")

punto1 = [int(x) for x in punto1.split(",")] # ['2', ' 2'] -> [2, 2]
punto2 = [int(x) for x in punto2.split(",")]

x1, y1 = punto1
x2, y2 = punto2
x3, y3 = x1, y2

"""
x1 = int(input("valor de x punto1: "))
y1 = int(input("valor de y punto1: "))

x2 = int(input("valor de x punto2: "))
y2 = int(input("valor de y punto2: "))
"""
distancia1 = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

print("el area del cuadrado es: ", distancia ** 2)
