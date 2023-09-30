def zipper(lista1, lista2):
    indice = 0
    listas_juntas = []

    if len(lista1) > len(lista2):
        lista_aux = lista1[:]
        lista1 = lista2[:]
        lista2 = lista_aux[:]
    
    
    for item in lista1:
        listas_juntas.append((item, lista2[indice]))
        indice += 1

    return listas_juntas


cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
siglas = ['BA', 'SP', 'MG', 'RJ']

print(zipper(siglas, cidades))

# Existe uma função zip() que faz isso automaticamente
