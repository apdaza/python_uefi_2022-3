from libreria_figuras import *

print("Primer punto")
p1 = capturar_punto()

print("Segundo punto")
p2 = capturar_punto()

figuras = ["circulo", "rectangulo", "triangulo"]

for f in figuras:
    area = calcular_area(p1, p2, f)
    perimetro = calcular_perimetro(p1, p2, f)
    print("El area del " + f + " es: " + str(area))
    print("El perimetro del " + f + " es: " + str(perimetro))