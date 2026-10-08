print("\nprimera")
suma = 0
contador = 0

while True:
    numero = float(input("Introduce un numero (0 para terminar): "))
    if numero == 0:
        break 
    suma = suma + numero
    contador = contador + 1

media = suma / contador if contador > 0 else 0
print(f"\nTotal: {suma}")
print(f"La Media: {media}")


print("\nsegunda")

suma = 0
contador = 0
numero = float(input("Introduce un numero (0 para terminar): "))

while numero != 0:
    suma = suma +numero
    contador = contador + 1
    numero = float(input("Introduce un numero (0 para terminar): "))

media = suma / contador if contador > 0 else 0

print(f"\nSuma total: {suma}")
print(f"Media de los números: {media}")
