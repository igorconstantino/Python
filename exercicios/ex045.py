import  random

lista_jogadas = ['Pedra', 'Papel', 'Tesoura']
jogada_pc = random.choice(lista_jogadas)
jogada_user = ''

print("""----- MENU -----
(1) - Pedra
(2) - Papel
(3) - Tesoura
""")
opcao_user = int(input('Digite sua jogada: '))

if opcao_user == 1:
    jogada_user = 'Pedra'
elif opcao_user == 2:
    jogada_user = 'Papel'
elif opcao_user == 3:
    jogada_user = 'Tesoura'
else:
    print('Digite uma jogada válida!')

# Definindo quem irá ganhar
if jogada_pc == 'Pedra':
    if jogada_user == 'Pedra':
        print('EMPATE!')
    elif jogada_user == 'Papel':
        print('GANHOU!')
    elif jogada_user == 'Tesoura':
        print('PERDEU!')
elif jogada_pc == 'Papel':
    if jogada_user == 'Pedra':
        print('PERDEU!')
    elif jogada_user == 'Papel':
        print('EMPATE!')
    elif jogada_user == 'Tesoura':
        print('GANHOU!')
elif jogada_pc == 'Tesoura':
    if jogada_user == 'Pedra':
        print('GANHOU!')
    elif jogada_user == 'Papel':
        print('PERDEU!')
    elif jogada_user == 'Tesoura':
        print('EMPATE!')
