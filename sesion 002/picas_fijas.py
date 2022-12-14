from random import randint

secreto = []

opciones = [3,4,5]
while True:
    cant_digitos = int(input("Ingrese la cantidad de digitos (3, 4 o 5):"))
    if cant_digitos in opciones:
        break
    else:
        print("cantidad de digitos no valida")

while True:
    n = randint(0, 9)
    if n == 0 and len(secreto) == 0:
        continue
    if n not in secreto:
        secreto.append(n)
    if len(secreto) == cant_digitos:
        break

print(secreto)

intentos = 0

while True:
    no_validado = True
    while no_validado:
        n = input("ingrese un número de " + str(cant_digitos) + "  digitos: ")
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

    if fijas == cant_digitos:
        print("Felicitaciones")
        break

    if intentos == len(secreto) * 2:
        print("Completaste los intentos permitidos")
        break

