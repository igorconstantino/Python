palavra = 'extintor'
lista_palavra = list(palavra)
palavra_codificada = []
lista_ocorrencias = []
contador = 0

for i in range(len(lista_palavra)):
    palavra_codificada.append('*')

while True:
    letra = input('Digite uma letra: ').strip()
    contador += 1

    if letra in palavra:
        for i in range(len(palavra)):
            if letra == palavra[i]:
                lista_ocorrencias.append(i)

    for i in range(len(lista_ocorrencias)):
        palavra_codificada[lista_ocorrencias[i]] = letra

    lista_ocorrencias.clear()

    nova_palavra = ''.join(palavra_codificada)

    print(f'A palavra se encontra assim: {nova_palavra}')

    if nova_palavra == palavra:
        break

print('PARABÉNS VOCÊ ACERTOU!!!')
print(f'Foram necessárias {contador} tentativas!')
