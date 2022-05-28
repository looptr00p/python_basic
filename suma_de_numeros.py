num1 = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese otro numero entero: "))
sum = 0
while num1 > num2:
    num1 = int(input("Ingrese un numero entero: "))
    num2 = int(input("Ingrese otro numero entero: "))
while num1 <= num2:
    sum = sum + num1
    num1 = num1 + 1
# for number in range(num1, num2 + 1):
#     sum = sum + number
print("La suma es = " + str(sum))