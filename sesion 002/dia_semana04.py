dias = ["lunes", "martes", "miercoles",
        "jueves", "viernes", "sabado", "domingo"]

dia = int(input("ingrese el día de la semana: "))

if dia >= 1 and dia <= 7:
    print(dias[dia - 1])
else:
    print("error día no válido")