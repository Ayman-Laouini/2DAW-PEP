
variable = 6
print("Tipo de la variable:", type(variable))


variable2 = variable
print("Tipo de la segunda variable:", type(variable2))


print("comprobacion de que la variable1 es la variable2:", variable is variable2)


variable = "Hola"
print("Nuevo tipo de la primera variable:", type(variable))


print("¿la primera variable es un texto?:", isinstance(variable, str))
print("¿var2 sigue siendo un entero?:", isinstance(variable2, int))