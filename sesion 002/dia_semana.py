dia = int(input("ingrese el día de la semana: "))

if dia > 7 or dia < 1:
    print("error día no válido")
else:
    if dia == 1:
        print("lunes")
    elif dia == 2:
        print("martes")
    elif dia == 3:
        print("miercoles")
    elif dia == 4:
        print("jueves")
    elif dia == 5:
        print("viernes")
    elif dia == 6:
        print("sabado")
    else:
        print("domingo")