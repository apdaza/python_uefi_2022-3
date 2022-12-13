from random import randint

secreto = []

while True:
    n = randint(0, 9)
    if n not in secreto:
        secreto.append(n)
    if len(secreto) == 3:
        break

print(secreto)

while True:
    n = input("ingrese un número de 3 digitos: ")
    numero = [int(c) for c in n]
    picas = 0
    fijas = 0

    for i in range(len(numero)):
        for j in range(len(secreto)):
            if secreto[j] == numero[i]:
                if j == i:
                    fijas += 1
                else:
                    picas += 1

    print("picas = ", picas, " fijas = ", fijas)

    if fijas == 3:
        print("Felicitaciones")
        break

