num = int(input('Digite um número para obter sua tabuada: '))

print('-' * 12)
for i in range(0, 11):
    print(f'{num} X {i} = {i * num}')
print('-' * 12)