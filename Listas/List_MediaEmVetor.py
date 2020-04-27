#Faça um Programa que peça as quatro notas de 10 alunos, 
# calcule e armazene num vetor a média de cada aluno, 
# imprima o número de alunos 
# com média maior ou igual a 7.0.

listaNotas = []
notasAlunos = []
cont = 0

for i in range(3):
  media = 0
  notasAlunos = []

  for j in range(4):
    notasAlunos.append(float(input("Nota: ")))
    media+=notasAlunos[j]
    print(media)
    print("Media: ",media/4) 
  media = media/4
  if media > 7.0:
    listaNotas.append(media)
    cont+=1

print("Quantidade de alunos com nota maior que 7.0: ",cont)

  