# Escribe un programa que le pida al usuario un número de hasta 4 dígitos y que te entregue la descomposición en Unidades, Decenas, Centenas y Miles. Ejemplos

#     Para 1230 debe imprimir: 1M + 2C + 3D + 0U
#     Para 36 debe imprimir: 3D + 6U
numero = input()
rev_numero = numero[::-1]
lista = ['U','D', 'C', 'M']
res = ''
for num in range(0, len(rev_numero)):
    if(num == 0):
        res = rev_numero[num] + lista[num] + res
    else:
        res = rev_numero[num] + lista[num] + " + "+ res
print(res)