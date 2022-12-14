from libreria_pyf import *

digitos = generar_cantidad()
print("vamos a jugar con %d digitos" % digitos)
intentos = 0
secreto = generar_secreto(digitos)
print(secreto)

while True:
    intentos += 1
    numero = capturar_numero(digitos)
    
    resultado = comparar(secreto, numero)
    print("intento %d (picas = %d, fijas = %d)" % (intentos, resultado[0], resultado[1]))
    if resultado[1] == digitos:
        print("Felicitaciones")
        break
    if intentos == digitos * 2:
        print("se terminaron los intentos")
        break