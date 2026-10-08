

print("Escribe un numero par primero y luego uno impar")

numeroPar = int(input("numero par: "))
numeroImpar = int(input("numero impar: "))

if numeroPar % 2 == 0:
    print("Correcto")
else:
    print("Incorrecto: El primer numero es impar")

if numeroImpar % 2 != 0:
    print("Correcto")
else:
    print("Incorrecto: El segundo numero es par")
