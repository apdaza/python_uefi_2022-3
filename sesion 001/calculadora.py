'''
programa que captura dos valores
y calcula las operaciones basicas

por alejandro daza
'''

# captura de variables
numero1 = int(input("ingrese el primer número: "))
numero2 = int(input("ingrese el segundo número: "))

# calculo de operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 // numero2

# muestra de resultado
print(numero1, " + ", numero2, " = ", suma)
print(numero1, " - ", numero2, " = ", resta)
print(numero1, " * ", numero2, " = ", multiplicacion)
print(numero1, " // ", numero2, " = ", division)