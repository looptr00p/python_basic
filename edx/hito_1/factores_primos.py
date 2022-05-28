#F
# 



# actores Primos
# Crea un programa que imprima la descomposición de factores primos de un número. 
# Tu programa recibirá como entrada un número entero y debe imprimir cada factor primo del número en una línea separada. 
# Por ejemplo para el número 22 debiera imprimir:
# 2
# 11

# 22
# 1,2,11,22

#30
#1, 3, 10 5, 6
# 3 5

# primos se dividen por 1 y por si mismo
#1 2 3 5 7 11 13 17 19 23 29 31

#funcion de obtener factores

#1.- 50 OK
numero = int(input())

def es_primo_1(num):
    if num <2:
        return False
    for k in range(2, num):
        if num %k ==0:
            return False
    return True
    
def obtenerFactores(numero):
    factores = []
    for n in range(1,numero +1):
        if numero%n == 0:
            factores.append(n)
    return factores
    
factores = obtenerFactores(numero)
if len(factores) == 2:
    print(factores[1])
else:
    factores.pop(0)
    factores.pop(len(factores) - 1)
    print(factores)
    for f in factores:
        esPrimo = es_primo_1(f)
        if(esPrimo):
            print(f)
