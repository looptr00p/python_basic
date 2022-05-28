#Contestador de celular
numero_telefono=input("Ingrese número teléfonico: ")
hora_llamada=int(input("Ingrese hora de la llamada: "))
while len(numero_telefono) != 8 or (hora_llamada < 0 or hora_llamada >= 24) :
#mientras el largo del numero telefonico sea distinto a 8 y 
#la hora de llamada sea menor a 0 y mayor a 24... vuelvo a pedir datos
  numero_telefono=input("Ingrese número teléfonico: ")
  hora_llamada=int(input("Ingrese hora de la llamada: "))
if hora_llamada >=0 and hora_llamada <=7:
  print("CONTESTAR")
elif hora_llamada <14 and numero_telefono[-3:] == "909":
  print("CONTESTAR")
elif hora_llamada <14:
  print("NO CONTESTAR")
elif hora_llamada >=17 and hora_llamada <=19 and numero_telefono [:3] == "877":
  print("NO CONTESTAR")
elif hora_llamada >=17 and hora_llamada <=19:
  print("CONTESTAR")
elif hora_llamada >19:
  print("NO CONTESTAR")