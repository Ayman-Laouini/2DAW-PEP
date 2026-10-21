#cuarto ejercicio Ayman Laouini 2ºDAW
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
    while radio <= 0:
        print("El radio debe ser mayor que 0")
        radio = float(input("Introduce el radio del circulo: "))
        
    area = calcular_area_circulo(radio)
    print("El area del círculo es:", area)

def opcion2():
    base = float(input("base del triangulo: "))
    while base <= 0:
        print(" La base debe ser mayor que 0")
        base = float(input("base del triangulo: "))
        
    altura = float(input("altura del triangulo: "))
  
    while altura <= 0:
        print("La altura debe ser mayor que 0")
        altura = float(input("altura del triangulo: "))
        
    area = calcular_area_triangulo(base, altura)
    print("El area del triangulo es:", area)

def opcion3():
    base = float(input("base del rectangulo: "))
  
    while base <= 0:
        print("La base debe ser mayor que 0")
        base = float(input("base del rectangulo: "))
        
    altura = float(input("altura del rectangulo: "))
 
    while altura <= 0:
        print("La altura debe ser mayor que 0")
        altura = float(input("altura del rectangulo: "))
        
    area = calcular_area_rectangulo(base, altura)
    print("El area del rectangulo es:", area)

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
