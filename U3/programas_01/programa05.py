#Quinto ejercicio Ayman Laouini 2ºDAW

pais = "España"

def mostrar_pais():
    print("Pais global:", pais)

def cambiar_pais():
    global pais
    pais = "Portugal"

def crear_ciudad():
    ciudad = "Madrid" 
    print("Ciudad local:", ciudad)

def funcion_externa():
    contador = 10 
    
    def funcion_interna():
        nonlocal contador
        contador = contador + 5
        print("modificado por funcion interna:", contador)
    
    print("antes de la funcion interna:", contador)
    funcion_interna()
    print("despues de la funcion interna:", contador)

def main():
    print("GLOBAL")
    mostrar_pais()
    print("Cambiando pais...")
    cambiar_pais()
    mostrar_pais()
    print()

    print("LOCAL")
    crear_ciudad()
    print()

    print("NO LOCAL")
    funcion_externa()

main()
