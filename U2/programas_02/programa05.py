
while True:
    numero = int(input("Introduce un numero entre 1 y 10: "))
    if 1 <= numero <= 10:
        break
    print("Numero incorrecto. Debe estar entre 1 y 10.")

print(f"Lista de numeros del 1 al {numero}:")
for i in range(1, numero + 1):    
    print(i)
    
