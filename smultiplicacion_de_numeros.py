response = "s"
while response == 's' or response == 'S':
    number = int(input("Ingresa un número del 1 al 9: "))
    while number < 1 or number > 9:
        number = int(input("Ingrese un número del 1 al 9: "))
    for x in range(1, 10):
        mult = number * x
        print(str(number) + " X " + str(x) + " = " + str(mult))
    response = input("¿Quieres introducir otro número? S=SI / N=NO: ")
print("Gracias por usar nuestro programa")