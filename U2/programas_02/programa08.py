import random

numero_secreto = random.randrange(1, 21)
intentos = 0

print("Adivina el numero entre 1 y 20. Tienes 3 intentos.")

while intentos < 3:

    numero_usuario = int(input("Introduce un número: "))
    intentos = intentos + 1 
    
    if numero_usuario == numero_secreto:
        print("Has acertado el numero")
        break

    elif numero_usuario < numero_secreto:
        print("El numero oculto es mayor")
    else:
        print("El numero oculto es menor")


if numero_usuario != numero_secreto:
    print("Te has quedado sin intentos, el numero era :", numero_secreto)
