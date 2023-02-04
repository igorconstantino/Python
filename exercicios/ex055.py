lista_pesos = []
maior = 0

for i in range(0, 5):
    peso = float(input('Qual o seu peso: '))
    lista_pesos.append(peso)
    lista_pesos.sort()
    maior = lista_pesos[len(lista_pesos) - 1]

print(f'O maior peso é {maior}Kg')
