dias = ["lunes", "martes", "miercoles",
        "jueves", "viernes", "sabado", "domingo"]

valido = True

while(valido):
    dia = int(input("ingrese el día de la semana: "))
    if dia >= 1 and dia <= 7:
        #valido = False
        break
    else:
        print("día no valido")

print(dias[dia - 1])
