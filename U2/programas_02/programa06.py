while True:
   
    while True:
        numero = int(input("Introduce un numero entre 1 y 10 : "))
        if 1 <= numero <= 10:
            break
        print("Error:Tiene que estar en el rango")
    

    print(f"\nTabla de multiplicar del {numero}")
    for i in range(1, 11):

        print(f"{numero} x {i} = {numero * i}")

    print("-\n")
    
  
    respuesta = input("¿Quieres introducir otro numero? (s/n): ").strip().upper()
    if respuesta != 'S':
        print("Programa finalizado")
        break 
