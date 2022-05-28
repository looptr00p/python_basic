#Aprobación de créditos
# Un Banco desea implementar una política de atención automatizada de créditos de consumo, y te contrata para programar su servicio. Los postulantes entregarán al banco la siguiente información:

#     Ingreso (en pesos)
#     Año de nacimiento
#     Número de hijos
#     Años de pertenencia al banco
#     Estado civil ("S": soltero, "C", casado)
#     Si vive en campo o cuidad ("U": urbano, "R": rural)


# El banco usará las siguientes reglas para decidir la aprobación del crédito, con una de ellas que se cumpla, se aprueba el crédito:

#     Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
#     Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
#     Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
#     Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
#     Si el cliente vive en el campo, es casado y tiene menos de dos hijos.

# Tu programa debe preguntar sus datos al cliente, procesarlos, e imprimir el mensaje APROBADO o RECHAZADO según corresponda
ingreso = int(input())
a_nacimiento = int(input())
edad = 2022 - a_nacimiento
num_hijos = int(input())
a_presencia_banco = int(input())
estado_civil = input()
lugar_recidencia = input()


if a_presencia_banco >= 10 and num_hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and num_hijos > 3 and edad >= 45 and edad <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and lugar_recidencia == "U":
    print("APROBADO")
elif ingreso > 3500000 and a_presencia_banco > 5:
    print("APROBADO")
elif lugar_recidencia == "R" and estado_civil == "C" and num_hijos < 2:
    print("APROBADO")
else:
    print ("RECHAZADO")

