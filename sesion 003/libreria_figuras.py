from math import sqrt, pi

def capturar_punto():
    x = int(input("ingrese el valor de x: "))
    y = int(input("ingrese el valor de y: "))
    return x, y

def calcular_distancia(punto1, punto2):
    return sqrt(((punto1[0] - punto2[0]) ** 2) +
                 ((punto1[1] - punto2[1]) ** 2)
                )

def calcular_area(punto1, punto2, figura = "rectangulo"):
    if figura == "rectangulo":
        temp = punto1[0], punto2[1]
        base = calcular_distancia(punto1, temp)
        altura = calcular_distancia(punto2, temp)
        area = base * altura
    elif figura == "circulo":
        radio = calcular_distancia(punto1, punto2)
        area = pi * radio ** 2
    else:
        area = None
    return area

def calcular_perimetro(punto1, punto2, figura = "rectangulo"):
    if figura == "rectangulo":
        temp = punto1[0], punto2[1]
        base = calcular_distancia(punto1, temp)
        altura = calcular_distancia(punto2, temp)
        perimetro = base * 2 + altura * 2
    elif figura == "circulo":
        radio = calcular_distancia(punto1, punto2)
        perimetro = pi * radio * 2
    else:
        perimetro = None
    return perimetro