salario_actual=int(input("Indique los años de antiguedad: "))
antiguedad=int(input("Indique los años de antiguedad: "))
if antiguedad <= 3:
    nuevo_salario = salario_actual * 1.5
elif antiguedad > 3 and antiguedad <= 6:
    nuevo_salario = salario_actual * 1.25
elif antiguedad > 6 and antiguedad <= 10:
    nuevo_salario = salario_actual * 1.35
else:
    nuevo_salario = salario_actual * 1.50
print("El nuevo salario del empleado es = " + str(nuevo_salario))