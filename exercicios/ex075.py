numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),
           int(input('Digite um número: ')),)

index_3 = numeros.index(3)

print(numeros)
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if index_3 == -1:
    print('O 3 não foi digitado')
else:
    print(f'O 3 está na posição {index_3 + 1}')
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
