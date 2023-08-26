"""Ejercicios Estructuras Condicionales:
Resolver cada enunciado utilizando las estructuras IF / ELSE / ELIF, según usted crea correspondiente:"""
#1. Pedirle al usuario que ingrese un número, si este es 10 se debe imprimir: ¡Usted haganado el sorteo!

numero = int(input("Ingrese un número: "))

if numero == 10:
    print("¡Usted ha ganado el sorteo! ... ¡Felicidades!")

#2. Sumar al ejercicio anterior, una pregunta: Si el número es menor imprimir: ¡Falto un poco, seguí participando! Si es mayor, imprimir: ¡Te pasaste, a seguir intentando!
elif numero < 10:
    print("¡Falto un poco, siga participando!")
else:
    print("¡Te pasaste, a seguir intentando!")


# #3. Pedirle al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes,otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje

dia = input("Ingrese un día de la semana: ")

if dia == "lunes":
    print("¡Hoy es lunes!")
elif dia in {'martes','miercoles','jueves'}:
    print ("Feliz jornada")
elif dia == "viernes":
    print("¡Hoy es viernes!")
elif dia == "sábado" or dia == "domingo":
    print("¡Hoy es fin de semana!")
else:
    print("¡Hoy no es lunes, viernes, sábado o domingo!")

# 4. Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre elmensaje “es vocal”

letra = input("Ingrese una letra: ")

if letra in {'a','e','i','o','u'}:
    print(f"¡la  letra {letra} Es una vocal!")
else:
    print(f"¡la  letra {letra} No es una vocal!")

'''Ejercicios Estructuras Repetitivas:
Resolver cada enunciado utilizando las estructuras FOR / WHILE, según usted crea
correspondiente:'''
# 1. Escribir un programa que realice la sumatoria de los números que se quiera ingresar,hasta que se ingrese -1

suma = 0

numero = int(input("Ingrese los números que desea sumar, (-1 para terminar): \n"))

while numero != -1:
    suma = suma + numero 
    numero = int(input("Ingrese los números que desea sumar, (-1 para terminar): \n"))
print("La suma de los números ingresados es", suma)

#2. Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números aintroducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

cantidad = int(input('\nIngrese la cantidad de números que desea introducir: '))

numeros_mayores = 0
numeros_menores = 0
numeros_cero = 0

for i in range(cantidad):
    numeroIntroducido = float(input(f'Ingrese los números: \n'))

    numeros_mayores += numeroIntroducido > 0
    numeros_menores += numeroIntroducido < 0
    numeros_cero += numeroIntroducido == 0

print(f" * Cantidad de números mayores a cero: {numeros_mayores}, \n * Cantidad de números menores a cero: {numeros_menores}, \n * Cantidad de números iguales a cero: {numeros_cero},\n")


# 3. Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un cero.

vocal = input("Ingrese una vocal o  0 para terminar ")

while vocal != "0":
    if vocal in {'a','e','i','o','u'}:
        print(f"¡la  letra {vocal} Es una vocal!")
    else:
        print(f"¡la  letra {vocal} No es una vocal!")
    vocal = input("Ingrese una vocal o  0 para terminar ")
print("Programa terminado!")


#4. Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

suma = 0
contador = 0
media = 0

numero = float(input("Introduce un número: "))

while numero != 0:
    suma = suma + numero 
    contador += 1
    media = suma/contador
    numero = float(input("Introduce un número: "))
print("Se han introducido", contador, "números que en total han sumado", suma)
print("La media es", media)
  


