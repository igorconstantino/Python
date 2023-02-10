def notas(*valores, situacao=False):
    """
    --> This function calculates the mean, the minimum, the maximum and the total grades of an student.
    :param valores: the student's grades
    :param situacao: (opcional) show the situation
    :return: return a dictionary of the student
    """
    aluno = {'total': len(valores),
             'maior': max(valores),
             'menor': min(valores),
             'média': sum(valores) / len(valores)}

    if situacao:
        if aluno['média'] < 3:
            aluno['situação'] = 'Ruim'
        elif aluno['média'] < 7:
            aluno['situação'] = 'Moderado'
        else:
            aluno['situação'] = 'Bom'

    return aluno


resposta = notas(5.5, 6.4, 10, 3.9, situacao=True)
print(resposta)
print('_' * 100)
help(notas)
