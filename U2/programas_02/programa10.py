import random

banca = random.randrange(17, 22)

num_jugadores = int(input("Introduce el numero de jugadores: "))


for i in range(1, num_jugadores + 1):
    print(f"\nTURNO DEL JUGADOR {i}")
    
    puntos_jugador = 0
    continuar = "S"
    
    while continuar == "S":

        carta = random.randrange(1, 6)
        puntos_jugador = puntos_jugador + carta

        print(f"Jugador {i}, te ha salido un: {carta} cartas totales: {puntos_jugador}")
        
        if puntos_jugador > 21:

            print("Te has pasado de 21")
            break
            
        continuar = input("¿Quieres otra carta? (S/N): ").upper()
    
  
    print(f"\nResultado Jugador {i}")
    print(f"Banca: {banca} | Jugador {i}: {puntos_jugador}")
    
    if puntos_jugador > 21:
        print(f"Resultado: El Jugador {i} pierde")
    elif puntos_jugador > banca:
        print(f"Resultado: El Jugador {i} gana a la banca")
    else:
        print(f"Resultado: El Jugador {i} pierde (la banca gana o empata)")

print("\nFIN DE LA PARTIDA")
