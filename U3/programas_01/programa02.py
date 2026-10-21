#Segundo ejercicio Ayman Laouini 2ºDAW

def saludar(nombre, primer_apellido, segundo_apellido, curso="2DAW"):
    print("Alumno:" ,nombre , "",primer_apellido , "" , segundo_apellido , "- Curso: " ,curso)

# Sin indicar el curso
saludar("Ayman", "Laouini", "Khalifa")


saludar("Lorena", "Sánchez", "Ruiz", "2DAW")

# parametros clave valor
saludar(segundo_apellido="Pérez", nombre="Laura", primer_apellido="Fernández")

# parametros nominales mixtos
saludar("Jorge", "Martínez", segundo_apellido="Marín", curso="2DAW")