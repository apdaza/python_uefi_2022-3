from random import randint

def generar_secreto(digitos):
    secreto = []
    while True:
        n = randint(0,9)
        if n == 0 and secreto == []:
            continue
        if not n in secreto:
            secreto.append(n)
        if len(secreto) == digitos:
            break
    return secreto

def capturar_numero(digitos):
    while True:
        numero = []
        n = input("Ingrese un número de %d digitos: " % digitos)
        if n[0] == '0':
            print("el número no puede iniciar con cero")
            continue
        for i in n:
            if int(i) not in numero:
                numero.append(int(i))
        if len(numero) == digitos:
            break
    return numero

def comparar(secreto, usuario):
    picas = 0
    fijas = 0

    for i in range(len(secreto)):
        for j in range(len(usuario)):
            if secreto[i] == usuario[j]:
                if i == j:
                    fijas += 1
                else:
                    picas += 1
    return picas, fijas