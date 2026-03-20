import colorama

colorama.init()

rojo = colorama.Fore.RED
azul = colorama.Fore.BLUE
verde = colorama.Fore.GREEN
amarillo = colorama.Fore.YELLOW
naranja = colorama.Fore.LIGHTRED_EX
reset = colorama.Style.RESET_ALL

print("Bienvenido al seleccionador")

while True:
    intro = int(input("Ingrese un numero (0 para salir): "))
    
    if intro == 0:
        print("Saliendo del programa...")
        break

    if 1 <= intro <= 10:
        print("Seleccionaste el numero " + str(intro))
    else:
        print(rojo + "Ingrese un numero valido" + reset)
        continue

    print("\nSelecciona un color:")
    print("1. Rojo")
    print("2. Azul")    
    print("3. Verde")
    print("4. Amarillo")
    print("5. Naranja")

    color = int(input("Ingrese un color: "))

    if color == 1:
        print(rojo + "Seleccionaste Rojo" + reset)
        color_nombre = "Rojo"
    elif color == 2:
        print(azul + "Seleccionaste Azul" + reset)
        color_nombre = "Azul"
    elif color == 3:
        print(verde + "Seleccionaste Verde" + reset)
        color_nombre = "Verde"
    elif color == 4:
        print(amarillo + "Seleccionaste Amarillo" + reset)
        color_nombre = "Amarillo"
    elif color == 5:
        print(naranja + "Seleccionaste Naranja" + reset)
        color_nombre = "Naranja"
    else:
        print(rojo + "Color no valido" + reset)
        continue

    print("Felicidades, ahora tienes un superduper " + color_nombre + " " + str(intro))