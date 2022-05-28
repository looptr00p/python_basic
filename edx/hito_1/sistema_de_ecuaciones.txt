# Escribe un programa que resuelva un sistema de dos ecuaciones con dos incognitas. 
# Tu programa recibirá los seis números reales que representan el sistema y 
# deberá imprimir la dos soluciones redondeadas a un decimal. 
# Ejemplo: Para el sistema 2x+3y=6 y x+2y=5, tu programa debe imprimir

#     x=-3.0
#     y=4.0

#Sistema de Ecuaciones

x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())

sx1 = x1 * x2
sx2 = x2 * -x1

sy1 = y1 * x2
sy2 = y2 * -x1

sr1 = r1 * x2
sr2 = r2 * -x1

# print(str(sx1)+ "x+" + str(sy1) + "y=" + str(sr1))
# print(str(sx2)+ "x+" + str(sy2) + "y=" + str(sr2))

y = sy1 + sy2
r = sr1 + sr2
y = float(y * r)
x = float((sr1 - y1 * y)/sx1)
print("['x=" + str(x) + "', 'y="+str(y)+"']")

# 2x+3y=6 y x+2y=5
#2x+3y=6  * 1
#1x+2y=5  * -2
#2x+3y=6
#-2x-4y=-10
#3y=6
#-4y=-10
#-y=-4
#4 = y

#2x+ 3*4 = 6
#2x + 12 = 6
#2x = -6
#x = -6/2
# x = -3





