import random

banca = random.randrange(17, 22)

puntos_jugador = 0
continuar = "S"

print("BLACKJACK")


while continuar == "S":

    carta = random.randrange(1, 6) 

    puntos_jugador = puntos_jugador + carta
    print(f"Te ha salido un: {carta}. Tus cartas suman: {puntos_jugador}")
    
    
    if puntos_jugador > 21:
        print("Te has pasado de 21,has perdido")
        break
    
    continuar = input("¿Quieres pedir otra carta? (S/N): ").upper()


print("\nResultado")

print(f"cartas totales de la banca: {banca}")
print(f"Tu puntuación: {puntos_jugador}")

if puntos_jugador > 21:
    print("Has perdido por pasarte de 21")
elif puntos_jugador > banca:
    print("Has ganado a la banca.")
else:
    print("Has perdido,la banca gana o empata.")
