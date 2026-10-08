

print("Escribe un numero par primero y luego uno impar")

numeroPar = int(input("numero par: "))

if numeroPar % 2 == 0:
    print("Correcto, ahora un numero impar")
else:
    print("Incorrecto: El numero es impar")


numeroImpar = int(input("numero impar: "))

if numeroImpar % 2 != 0:
    print("Correcto, es un numero impar")
else:
    print("Incorrecto: El numero es par")
