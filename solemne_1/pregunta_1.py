tiempo = int(input("Ingrese el instante de tiempo t: "))
velocidad_incial = 10
velocidad_final = 20
aceleracion = int((velocidad_final - velocidad_incial) / tiempo)
posion = int(velocidad_incial * tiempo + ((aceleracion * (tiempo * tiempo))/2))
print("La aceleracion de la particula es " + str(aceleracion) + " y la posición es: " + str(posion))