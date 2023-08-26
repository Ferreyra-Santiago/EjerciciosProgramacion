# """
# Crear lista 
# 1. Con los nombres de su familia.
# 2. Con los valores de la temperatura de un mes entero (mes a elección, pero definirlo).
# 3. Con los nombres de ciudades que hayan visitado.
# 4. Con las fechas y nombres de eventos importantes de su vida.

# Luego:
# 5. Ordenar alfabéticamente la lista de los nombres de familia.
# 6. Ordenar ascendentemente la lista de temperaturas.
# 7. Agregar en la lista de temperaturas, las temperaturas de los 15 días del mes siguiente.
# 8. Quitar de la lista de los nombres de familia, a tus abuelos.
# 9. Quitar de la lista de ciudades la ciudad menos linda que hayas visitado. atraves de la posision 

# 10. Ejercicios Tuplas:
# Crear tres tuplas con datos random.
# Crear una lista que las contenga y mostrarla.

# Ejercicio Diccionarios:
# Crear el siguiente diccionario:
# 11. Las claves serán los dni de su núcleo familiar, y el valor será SOLO el nombre de la persona.
# Luego deberán añadir los datos de familia ampliada (abuelos, familia política, etc)
# 12. Crear un nuevo diccionario con claves autogeneradas y valores de números de teléfono.
# Ambos deben ser mostrados.
# """


# #1
# familia = ["Santiago", "Adriana", "Roberto","Franco","Micaela","Hector","Angela"]
# print(familia)

# #2

# marzo = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 27, 26, 20, 25, 23, 20, 27, 28, 30, 26, 23 ,19 , 22, 28 , 31, 28 , 25, 23 , 21 ]
# print(marzo)


# 3# 
# Ciudades_Conocidas = [ "Cordoba", "Salta", "Villa carlos paz", "Villa de las rosas", "Salsipuedes", "San francisco" ]

# 4#
# Eventos_importantes = ["Nacimiento 23/03/2002", "Cumpleaños 23/03", "Graduacion 17/12/2021", "Comienzo de estudio 01/03/2023", "Comienzo de trabajo 29/08/2023"]


# print("---------------------------------------------------------------")
# #5
# familia.sort()
# print("Ordenado Alfabeticamente", familia)	  

# #6
# marzo.sort()
# print("Ordenado Ascendentemente", marzo)

# #7
# marzo.extend([20, 21, 25, 18, 19, 22, 23, 20, 18, 16, 18])
# print("Lista de temperaturas con los 15 dias del mes siguiente", marzo)

# #8
# familia.remove("Hector")
# familia.remove("Angela")
# print("Lista de familiares sin los abuelos", familia)

# 9#
# del Ciudades_Conocidas[4] #metodo del para eliminar por posicion
# print("Lista de ciudades  linda", Ciudades_Conocidas)


# #10
# tupla1 = ("Sistema","botella","Windows",16)
# tupla2 = ("Guitarra","mesa","silla","botella")
# tupla3 = ("vaso","tablet","celular", "Android")

# lista = [tupla1, tupla2, tupla3] 
# print(lista)

# #11
# diccionario = {4654654654:"Santiago", 2725456465:"Adriana", 5484632:"Roberto", 79845321:"Franco", 234154:"Micaela"}
# print(diccionario)

# diccionario[165487321] = "Hector"
# diccionario[198753431] = "Angela"

# print(diccionario)

# #12
# import random
# numeros_telefono = {}

# for i in range(5):
#     clave = f"persona{i + 1}"
#     numero = "5" + "".join(str(random.randint(0, 9)) for i in range(8))
#     numeros_telefono[clave] = numero

# print(numeros_telefono) 
