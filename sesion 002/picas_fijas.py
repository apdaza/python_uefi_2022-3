from random import randint

secreto = []

while True:
    n = randint(0, 9)
    if n not in secreto:
        secreto.append(n)
    if len(secreto) == 3:
        break

print(secreto)

intentos = 0

while True:
    no_validado = True
    while no_validado:
        n = input("ingrese un número de 3 digitos: ")
        if len(n) != len(secreto):
            print("Número no valido")
            continue
        lista = [int(c) for c in n]
        numero = []
        for i in lista:
            if i not in numero:
                numero.append(i)
        if len(numero) == len(secreto):
            break
        print("Número no valido")

    picas = 0
    fijas = 0

    for i in range(len(numero)):
        for j in range(len(secreto)):
            if secreto[j] == numero[i]:
                if j == i:
                    fijas += 1
                else:
                    picas += 1

    intentos += 1
    print("picas = ", picas, " fijas = ", fijas, " intentos = ", intentos)

    if fijas == 3:
        print("Felicitaciones")
        break

    if intentos == len(secreto) * 2:
        print("Completaste los intentos permitidos")
        break

