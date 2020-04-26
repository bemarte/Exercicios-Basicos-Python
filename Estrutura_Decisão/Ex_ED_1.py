#Faça um Programa que leia três números e mostre o maior deles.
listaNum = [] 
listaNum =input("Insira números: ").split(",")
num = int(max(listaNum))
print(num)