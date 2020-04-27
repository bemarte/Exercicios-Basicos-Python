#Faça um programa que receba dois números inteiros e 
# gere os números inteiros que estão no intervalo 
# compreendido por eles.

num1 = int(input("Insira o numero x: "))
num2 = int(input("Insira o numero y: "))

lista = range(num1,num2+1)

for item in lista:
  print(item,end=" ")