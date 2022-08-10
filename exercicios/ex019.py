import random
nome1 = input('Nome do aluno: ')
nome2 = input('Nome do aluno: ')
nome3 = input('Nome do aluno: ')
nome4 = input('Nome do aluno: ')

lista = [nome1, nome2, nome3, nome4]
nomeEscolhido = random.choice(lista)
print(nomeEscolhido)
