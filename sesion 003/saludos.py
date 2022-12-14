def saludar(nombre, saludo = "Hola"):
    print(saludo + " " + nombre)

def saludar_grupo(grupo):
    for n in grupo:
        saludar(n)

def saludar2(*nombres):
    for n in nombres:
        saludar(n, "te saludo")

def saludar3(**parametros):
    for parametro, valor in parametros.items():
        print(parametro, " = ", valor)

if __name__ == "__main__":
    saludar("Alejandro")
    saludar("Maria", "buen día")

    saludar_grupo(['Juan', 'Pedro', 'Ana'])
    saludar_grupo(['Angelo', 'Luis'])

    saludar2('diana')
    saludar2('marcela','francia','paolo')

    saludar3(nombre='Alejo', saludo="Hi", edad='49')

    s = saludar("Juan")
    print(s)