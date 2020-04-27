#Faça um programa que imprima na tela os números de 1 a 20, 
# um abaixo do outro. Depois modifique o programa para que 
# ele mostre os números um ao lado do outro.

lista = range(1,21)

for item in lista:
  print(item)

for item in lista:
  print(item,end=" ")