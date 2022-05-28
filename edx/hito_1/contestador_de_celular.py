#Contestador de celular
num = input()
h = int(input())
if(h >= 19 and h <= 23):
  print("NO CONTESTAR")
elif h >= 0 and h <= 7:
  print("CONTESTAR")
elif h < 14 and num[-3:] == "909":
  print("CONTESTAR")
elif h < 14:
  print("NO CONTESTAR")
elif h >= 17 and h <= 19 and num[:3] == "877":
  print("NO CONTESTAR")
elif h >= 17 and h <= 19:
  print("CONTESTAR")
