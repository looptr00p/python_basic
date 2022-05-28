count = 0
sum = 0
number = int(input("Ingrese un numero positivo: "))
while number != 0:
    if count == 0:
        minor = number
        major = number
    else:
        if number < minor:
            minor = number
        if number > major:
            major = number
    sum = sum + number
    count = count + 1
    number = int(input("Ingrese un número positivo: "))
average = sum/count
print("La cantidad de nueros leidos son: ", + str(count))
print("El numero menor es: ", + str(minor))
print("El numero mayor es:  ", + str(major))
print("El promedio es:  ", + str(average))
