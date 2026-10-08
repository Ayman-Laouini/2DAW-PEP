
nota = int(input("Escribe un número entero entre 1 y 10: "))

#la variable coge la nota y la introduce al match

match nota:
    case variable if nota < 5: 
        print("Insuficiente:", nota)
    case variable if 5 <= nota < 6:
        print("Suficiente:", nota)
    case variable if 6 <= nota < 7:
        print("Bien:", nota)
    case variable if 7 <= nota < 9: 
        print("Notable:", nota)
    case variable if 9 <= nota <= 10:
        print("Sobresaliente:", nota)
    case _:
        print("Error: no es válida")
