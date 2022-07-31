aluno = {}

aluno['Nome'] = input('Nome do aluno: ').title()
aluno['Media'] = float(input(f'Media de {aluno["Nome"]}: '))
# verificando se a media é maior ou n q 7
if aluno['Media'] < 7:
    aluno['Situaçao'] = 'Reprovado'
else:
    aluno['Situaçao'] = 'Aprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}.')
