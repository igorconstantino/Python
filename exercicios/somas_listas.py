lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_somas = []

lista_zippada = list(zip(lista_a, lista_b))

for dupla in lista_zippada:
    lista_somas.append(dupla[0] + dupla[1])

print(lista_somas)
