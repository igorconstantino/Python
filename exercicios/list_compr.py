lista = [i if i % 2 == 0 else -i for i in range(20) if not i % 4 == 0]
print(lista)

################################################

nomes = ['Igor', 'Darma', 'Caio', 'Jean']
lista2 = [(x, y) for x in nomes for y in nomes if x != y]
print(lista2)

################################################

dicionario = {'nome': 'Igor', 'idade': 21}
lista3 = [(key, value) for key, value in dicionario.items()]
print(lista3)
