frase = str(input('Digite uma frase: ')).strip()
print('Ocorrência de letras "a": ', frase.lower().count('a'))
print('Posição em que "a" aparece pela primeira vez: ', frase.lower().find('a'))
print('Posição em que "a" aparece pela última vez: ', frase.lower().rfind('a'))
