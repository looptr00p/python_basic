temperaturas=[]
suma=0
for x in range(7):
    temperaturas.append(int(input("Ingrese la temperatura# " + str(x+1) + ": ")))
    if x==0:
        t_mayor=temperaturas[x]
        t_menor=temperaturas[x]
        dia_mayor=x
        dia_menor=x
    else:
        if temperaturas[x] > t_mayor:
            t_mayor=temperaturas[x]
            dia_mayor=x
        if temperaturas[x] < t_menor:
            t_menor=temperaturas[x]
            dia_menor=x
    suma=suma+temperaturas[x]
promedio=suma/len(temperaturas)
print("La cantidad de datos almacenados son: " + str(len(temperaturas)))
print("La temperatura mayor es = " + str(t_mayor))
print("La temperatura menor es = " + str(t_menor))
print("El promedio de temperaturas de la semana es = " + str(promedio))
if dia_mayor==0:
    print("El lunes ocurrió la temperatura mayor")
elif dia_mayor==1:
    print("El martes ocurrió la temperatura mayor")
elif dia_mayor==2:
    print("El miércoles ocurrió la temperatura mayor")
elif dia_mayor==3:
    print("El juevas ocurrió la temperatura mayor")