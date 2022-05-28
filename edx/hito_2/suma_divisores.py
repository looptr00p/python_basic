# Crea una función que calcule la suma de los divisores de un número sin incluir al número, llamada suma_divisores.
# Junto con la suma de los divisores haz que la función retorne si el número es primo o no,
# basándose en que si la suma de sus divisores es 1, el número es primo.

# completa el código de la función
def suma_divisores(numero):
    divisores = []
    for n in range(1,numero-1):
        if numero % n == 0:
            print(n)
            divisores.append(n)
    return sum(divisores)

numero = int(input())
r = suma_divisores(numero)
print(r)