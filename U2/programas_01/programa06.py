
dia = int(input("Introduce el dia: "))
mes = int(input("Introduce el mes: "))
ano = int(input("Introduce el año: "))


dias_maximos = 0

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    dias_maximos = 31


if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dias_maximos = 30

if mes == 2:

    if ano % 4 == 0:
        dias_maximos = 29
    else:
        dias_maximos = 28


if mes < 1 or mes > 12:
    print("La fecha es incorrecta")
if dia < 1 or dia > dias_maximos:
    print("La fecha es incorrecta")
if ano < 1:
    print("La fecha es incorrecta")
else:
    print("La fecha es correcta")
