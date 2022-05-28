# Crea un programa para el juego adivina mi número. Tú programa debe comenzar por generar aleatoriamente un número entre 1 y 20.
#  El jugador tiene 5 intentos para adivinar el número. En cada intento tu programa debe indicar si el número ingresado es menor
#  o mayor que el número secreto, imprimiendo el mensaje mi número es menor o mi número es mayor, según corresponda. 
# Cuando el jugador adivina el número o cuando se superan los intentos permitidos tu programa debe terminar e indicar al jugador:

#     Si adivinó el número debe decir "Adivinaste, mi número era " e indicar el número secreto.
#     Si no adivinó antes que se acabaran los intentos, tu programa debe decir "No adivinaste, mi número era " 
#       e indicar el número secreto.

import random

numero_secreto = random.randint(1,20)
intentos = 0

while intentos < 5:
    numero = int(input("Ingresa un numero: "))
    if numero < numero_secreto:
        print("Mi número es mayor")
        intentos += 1
    elif numero > numero_secreto:
        print("Mi número es menor")
        intentos += 1
    elif numero == numero_secreto:
        print("Adivinaste, mi número era " + str(numero_secreto))
        intentos = 6
if intentos == 5:
    print("No adivinaste, mi número era " + str(numero_secreto))