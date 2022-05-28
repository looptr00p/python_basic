# 3 2 1 
# 1 2 3
numero1 = int(input("Ingrese numero 1: ")) # 22
numero2 = int(input("Ingrese numero 2: ")) # 2
numero3 = int(input("Ingrese numero 3: ")) # 58

# max y min => sacar el numero máximo y numero mínimo

numero_mayor = max(numero1, numero2, numero3) # 58
numero_menor = min(numero1, numero2, numero3) # 2
numero_medio = (numero1 + numero2 + numero3) - (numero_mayor + numero_menor) # (22 + 2 + 58) - (58 + 2)

print(str(numero_menor) + ','+ str(numero_medio) + ',' + str(numero_mayor))