# lista = [['igor', [4, 5.6]], ['cindy', [4.5, 8]]]
#          [0][0]   [0][1][0]

lista = []
pessoa = []
notas = []

while True:
    nome = input('Digite o nome da pessoa: ').strip()
    nota1 = int(input('Digite a nota 1 do aluno: '))
    nota2 = int(input('Digite a nota 2 do aluno: '))

    notas.append(nota1)
    notas.append(nota2)

    pessoa.append(nome)
    pessoa.append(notas[:])

    lista.append(pessoa[:])

    notas.clear()
    pessoa.clear()

    op = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if op != 'S':
        break

print('N°  Nome        Média')
print('_' * 30)

for i, pessoa in enumerate(lista):
    print(f'{i:<4} {pessoa[0]:<10} {(pessoa[1][0] + pessoa[1][1]) / 2:>8}')

print('_' * 30)

while True:
    escolhido = int(input('Mostrar notas de qual aluno? (999 interrompe)'))

    if escolhido == 999:
        break

    print(f'As notas dele(a) são: {lista[escolhido][1]}')
    print('_' * 30)
