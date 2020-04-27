#Faça um Programa que leia um número e exiba o 
# dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), 
# se digitar outro valor deve aparecer valor inválido.

data = input("Insira um dia da semana: ")

if data =="1":
  print("Domingo")
elif data =="2":
  print("Segunda")
elif data =="3":
  print("Terça")
else:
  print("Valor inválido")