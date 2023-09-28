import copy

# 1)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = copy.deepcopy(produtos)

for item in novos_produtos:
    item['preco'] = round(item['preco'] * 1.1, 2)

print(novos_produtos, '\n')

#2)
produtos_ordenados_nome = copy.deepcopy(produtos)
produtos_ordenados_nome.sort(key=lambda chave: chave['nome'], reverse=True)

print(produtos_ordenados_nome, '\n')

#3)
produtos_ordenados_preco = copy.deepcopy(produtos)
produtos_ordenados_preco.sort(key=lambda chave: chave['preco'])

print(produtos_ordenados_preco)
