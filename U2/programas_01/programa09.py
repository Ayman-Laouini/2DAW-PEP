import random

print("Juego:Piedra,Papel o Tijera")
print("1- Piedra")
print("2- Papel")
print("3- Tijera")

usuario = int(input("Que vas a sacar: "))

ordenador = random.randrange(1, 4)

if ordenador == 1:
    print("El ordenador ha elegido: Piedra")
elif ordenador == 2:
    print("El ordenador ha elegido: Papel")
else:
    print("El ordenador ha elegido: Tijera")

if usuario == ordenador:
    print("Empate")
elif usuario == 1 and ordenador == 3:
    print("Has ganado Piedra gana a tijera")
elif usuario == 2 and ordenador == 1:
    print("Has ganado Papel gana a piedra")
elif usuario == 3 and ordenador == 2:
    print("Has ganado Tijera gana a papel")
else:
    print("Has perdido El ordenador gana")
