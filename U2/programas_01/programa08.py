import random

dado1Jugador1 = random.randrange(1, 7)
dado2Jugador1 = random.randrange(1, 7)

totalJugador1 = dado1Jugador1 + dado2Jugador1

maxJugador1 = max(dado1Jugador1, dado2Jugador1)

dado1Jugador2 = random.randrange(1, 7)
dado2Jugador2 = random.randrange(1, 7)

totalJugador2 = dado1Jugador2 + dado2Jugador2

maxJugador2 = max(dado1Jugador2, dado2Jugador2)

print("Jugador 1: Sacó", dado1Jugador1, "y", dado2Jugador1, "(Total =", totalJugador1, ", Dado más alto =", maxJugador1, ")")
print("Jugador 2: Sacó", dado1Jugador2, "y", dado2Jugador2, "(Total =", totalJugador2, ", Dado más alto =", maxJugador2, ")")
print("-" * 50)

if totalJugador1 > totalJugador2:
    print("Gana el Jugador 1 ")

elif totalJugador2 > totalJugador1:
    print("Gana el Jugador")
else:
    print("Empate")
    if maxJugador1 > maxJugador2:
        print("Gana el Jugador 1")
    elif maxJugador2 > maxJugador1:
        print("Gana el Jugador 2")
    else:
        print("Ambos empatan")
