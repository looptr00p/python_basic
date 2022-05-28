#Suma de los N primeros números
n = int(input())
suma = 0
for x in range(n + 1):
   suma = x + suma
print(suma)