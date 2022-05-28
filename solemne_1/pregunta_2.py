cantidad_habitantes = int(input("Cantidad total de habitantes: "))
ingreso_total_hogar = int(input("Ingrese el ingreso total del hogar: "))
total_personas_tercera_edad = int(input("Total personas de la tercera edad: "))

while total_personas_tercera_edad > cantidad_habitantes:
    print("No pueden haber mas adultos mayores que el total de habitantes declarados, por favor ingrese los datos nuevamnte.")
    cantidad_habitantes = int(input("Cantidad total de habitantes: "))
    ingreso_total_hogar = int(input("Ingrese el ingreso total del hogar: "))
    total_personas_tercera_edad = int(input("Total personas de la tercera edad: "))

ingreso_per_capita = ingreso_total_hogar/cantidad_habitantes

nivel_socio_economico = ''
if total_personas_tercera_edad >= 2 :
    nivel_socio_economico = 'C3'
elif cantidad_habitantes <= 4:
    if ingreso_per_capita <= 60000:
        nivel_socio_economico = 'C3'
    elif ingreso_per_capita > 60000 and ingreso_per_capita <= 100000:
        nivel_socio_economico = 'C2'
    elif ingreso_per_capita > 100000 and ingreso_per_capita <= 300000:
        nivel_socio_economico = 'C1'
    elif ingreso_per_capita > 300000:
        nivel_socio_economico = 'AB'
elif cantidad_habitantes >= 5:
    if ingreso_per_capita <= 40000:
        nivel_socio_economico = 'C3'
    elif ingreso_per_capita > 40000 and ingreso_per_capita <= 80000:
        nivel_socio_economico = 'C2'
    elif ingreso_per_capita > 80000 and ingreso_per_capita <= 250000:
        nivel_socio_economico = 'C1'
    elif ingreso_per_capita > 250000:
        nivel_socio_economico = 'AB'

print("Su nivel socio economico es " + nivel_socio_economico)