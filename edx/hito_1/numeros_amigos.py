# Dos números a y b se dicen números amigos, si la suma de los divisores de uno de los números es igual al otro número 
# y viceversa (en el cálculo de los divisores, no debes considerar al mismo número). 
# Crea una función que reciba 2 números, y retorne True si es que estos son amigos, y False si es que no lo son.

# completa el código de la función
def amigos(a,b):
  divisor = 1
  suma_divisores_a = 0
  suma_divisores_b = 0
  while divisor < a or divisor < b :
    if divisor < a:
      if a % divisor == 0:
        suma_divisores_a += divisor
    if divisor < b:
      if b % divisor == 0:
        suma_divisores_b += divisor
    divisor += 1
  print("A::" + str(suma_divisores_a))
  print("B::" + str(suma_divisores_b))
  if suma_divisores_a == b or suma_divisores_b == a:
    return True
  else:
    return False

a = int(input())
b = int(input())
amigos(a,b)