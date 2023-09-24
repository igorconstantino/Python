# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Qual a raiz quadrada de 25?',
        'Opções': ['1', '9', '4', '5'],
        'Resposta': '3',
    },
    {
        'Pergunta': 'Qual a fórmula do sal de cozinha?',
        'Opções': ['H2O', 'NaCl', 'CO2', 'C6h12O6'],
        'Resposta': '1',
    },
    {
        'Pergunta': 'O causador da giardíase é?',
        'Opções': ['Parasita', 'Protozoário', 'Vírus', 'Bactéria'],
        'Resposta': '1',
    },
]

# perguntas = [ { , ,[] }, { { , ,[] }, ... ]

contador = 0

for pergunta in perguntas:
    print(f'\n\nPergunta:  {pergunta["Pergunta"]}\n')
    
    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i}) {opcao}')
    
    op = input('\nDigite a opção escolhida: ')

    if op == pergunta['Resposta']:
        print('ACERTOU!')
        contador += 1
    else:
        print('ERROU!')

print(f'\nVocê acertou {contador} perguntas')
