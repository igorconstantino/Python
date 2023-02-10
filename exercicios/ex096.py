def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área do terreno de dimensões {largura}m x {comprimento}m é: {area}m²')


largura = float(input('Digite a largura do terreno (m): '))
comprimento = float(input('Digite a altura do terreno (m): '))
area(largura, comprimento)
