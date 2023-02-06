palavras = ('palavras', 'amor', 'baixinho', 'coraçao', 'escola', 'feijao', 'lanchonete', 'cacto')

for palavra in palavras:
    vogais = 'aeiou'
    print(f'\nNa palavra {palavra.upper()} temos: ', end='')

    for letra in range(len(palavra)):
        if palavra[letra] in vogais:
            print(f'{palavra[letra]} ', end='')
