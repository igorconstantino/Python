# jogadores = [{'nome': 'Igor', 'gols': [0, 1, 2, 3], 'total': 6},
#              {'nome': 'Thamires', 'gols': [1, 1, 2, 2], 'total': 6}]

jogadores = []
jogador = {}
gols = []

while True:
    nome = input('Digite o nome do jogador: ').strip().title()
    qtd_partidas = int(input(f'Quantas partidas {nome} jogou: '))

    for i in range(qtd_partidas):
        gols.append(int(input(f'Quantos gols jogou na partida {i + 1}: ')))

    jogador['nome'] = nome
    jogador['qtd'] = qtd_partidas
    jogador['gols'] = gols.copy()
    jogador['total'] = sum(gols)

    jogadores.append(jogador.copy())

    gols.clear()

    op = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if op == 'N':
        break

print('=' * 50)
print(f'{"Cod.":<5}{"Nome":<10}{"Gols":^10}{"Total":<50}')
print('_' * 50)
for i, jogador in enumerate(jogadores):
    print(f'{i:<5}{jogador["nome"]:<10}{jogador["gols"]}{jogador["total"]:<30}')
print('_' * 50)
op_jogador = int(input('Mostrar os dados de qual jogador?: '))
while op_jogador != 999:
    for i in range(jogadores[op_jogador]['qtd']):
        print(f'No jogo {i + 1} fez {jogadores[op_jogador]["gols"][i]} gols.')
    op_jogador = int(input('Mostrar os dados de qual jogador?: '))
