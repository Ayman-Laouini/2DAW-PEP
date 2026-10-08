while True:
    try:

        numero = int(input("Introduce un numero entre 1 y 10: "))

        if 1 <= numero <= 10:
            print(f"Esta en el rango")
            break 
        else:
            print("error, Intentalo de nuevo.")

    except ValueError:

        print("introduce un numero entero.")
