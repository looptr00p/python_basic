# Escribe un programa que reciba como entrada un número decimal e imprima el resultado de convertirlo a binario. 
# Por ejemplo, al ingresar el número 33 tu programa debiera imprimir el siguiente mensaje:
# resultado=100001

#Conversión de Decimal a Binario
decimal = int(input())
lista_modulos = []
while decimal != 0:
    modulo = decimal % 2
    cociente = decimal // 2
    #print("COCIENTE::: " + str(cociente))
    lista_modulos.append(str(modulo))
    decimal = cociente
print("resultado=" + "".join(lista_modulos[::-1]))