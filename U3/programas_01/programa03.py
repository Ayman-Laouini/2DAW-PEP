#tercer ejercicio Ayman Laouini 2ºDAW
import math

def calcular_area_circulo(radio):
    resultado = math.pi * (radio * radio)
    return resultado

def calcular_area_triangulo(base, altura):
    resultado = (base * altura) / 2
    return resultado

def calcular_area_rectangulo(base, altura):
    resultado = base * altura
    return resultado

def mostrar_menu():
    print("1. area de un circulo")
    print("2. area de un triangulo")
    print("3. area de un rectangulo")
    print("4. Salir")

def opcion1():
    radio = float(input("Introduce el radio del circulo: "))
    if radio > 0:
        area = calcular_area_circulo(radio)
        print("El area del círculo es:", area)
    else:
        print("El radio debe ser mayor que 0")

def opcion2():
    base = float(input("base del triangulo: "))
    altura = float(input("altura del triangulo: "))
    if base > 0 and altura > 0:
        area = calcular_area_triangulo(base, altura)
        print("El area del triangulo es:", area)
    else:
        print("La base y la altura deben ser mayores que 0")

def opcion3():
    base = float(input("base del rectangulo: "))
    altura = float(input("altura del rectangulo: "))
    if base > 0 and altura > 0:
        area = calcular_area_rectangulo(base, altura)
        print("El area del rectangulo es:", area)
    else:
        print("La base y la altura deben ser mayores que 0")

def main():
    opcion = 0
    while opcion != 4:

        mostrar_menu()
        opcion = int(input("Introduce una opcion (1-4): "))
        
        if opcion == 1:
            opcion1()
        elif opcion == 2:
            opcion2()
        elif opcion == 3:
            opcion3()
        elif opcion == 4:
            print("Saliendo del programa")
        else:
            print("Opcion incorrecta, vuelve a intentarlo.")


main()
