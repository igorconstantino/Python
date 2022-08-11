nome = input('Qual o seu nome?')
print(nome.upper())
print(nome.lower())
print('Número de caracteres(sem o espaço): ', len(nome) - nome.count(' '))

nomeDividido = nome.split()
tamPrimeiroNome = len(nomeDividido[0])

print('Primeiro nome tem {} letras'.format(tamPrimeiroNome))
