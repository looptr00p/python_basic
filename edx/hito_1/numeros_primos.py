# Escribe una función llamada es_primo que retorne True cuando un número es primo y False cuando no lo es.
# por favor escribe aquí tu función

def es_primo(numero):
    divisor = 1
    lista_divisores = []
    while divisor <= numero:
        if numero % divisor == 0:
            lista_divisores.append(divisor)
        divisor += 1
    #print(lista_divisores)
    #print(len(lista_divisores))
    if len(lista_divisores) == 2:
        return True
    else:
        return False

numero = int(input())
es_primo(numero)