#A série de Fibonacci é formada pela seqüência 
# 0,1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa que gere a série até que o 
# valor seja maior que 500.

num = 500

x,y = 0,1
while y < 1000:
  print(y,end=" ")
  x,y = y, x+y