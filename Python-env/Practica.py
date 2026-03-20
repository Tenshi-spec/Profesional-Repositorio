
while True:
    print("Bienvenido, esto solo es una practica simple de python")
    opcion = input("Presiona 1 para continuar o cualquier otra tecla para salir: ")
    if opcion != "1":
        Texto = input("Escribe lo que sea: ")
        print("selecciona un color para el texto: ")
        print("1. Rojo")
        print("2. Verde")
        print("3. Cyan")
        color_texto = int(input("Ingresa el número del color: "))
        if color_texto == 1:
            print("\033[31m" + Texto + "\033[0m")
        elif color_texto == 2:
            print("\033[32m" + Texto + "\033[0m")       
        elif color_texto == 3:
            print("\033[36m" + Texto + "\033[0m")
        else:        
            print("Opción de color no válida. Mostrando texto sin color.")
            print(Texto)
    else:
        print("¡Gracias por usar esta practica de python! ¡Hasta luego!")
        break