import random
nome1 = input('Digite o nome: ')
nome2 = input('Digite o nome: ')
nome3 = input('Digite o nome: ')
nome4 = input('Digite o nome: ')
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print(lista)
