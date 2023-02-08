aluno = {}

aluno['nome'] = input('Digite o nome do aluno: ').strip().capitalize()
aluno['média'] = float(input(f'Digite a média de {aluno["nome"]}: '))

if aluno['média'] >= 5:
    aluno['situação'] = 'aprovado'
else:
    aluno['situação'] = 'reprovado'

print(f'\nO aluno {aluno["nome"]} ficou com média {aluno["média"]} e está {aluno["situação"]}.')
