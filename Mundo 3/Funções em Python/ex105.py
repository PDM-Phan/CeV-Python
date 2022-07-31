def notas(*num, sit=False):
    """
    -> Funçao para analisar notas e situaçoes dos alunos.
    :param num: Notas de um ou mais alunos ( aceita varias )
    :param sit: Valor opcional, indicando se deve ou nao adicionar a situaçao
    :return: Dicionario com varias informaçoes sobre a situaçao da turma
    """
    n = {}
    notas = []
    maior = menor = 0
    for nu in num:
        notas.append(nu)
        if len(notas) == 1: # se tiver apenas 1 num
            maior = nu
            menor = nu
        else: # caso tiver 2 ou mais
            if nu > maior:
                maior = nu
            elif nu < menor:
                menor = nu
    m = sum(notas) / len(notas)
    n['Total'] = len(notas)
    n['Maior'] = maior
    n['Menor'] = menor
    n['Media'] = m
    if sit: # se quiserem mostrar a situaçao
        if m >= 7:
            n['Situaçao'] = 'BOA'
        elif 5 < m < 7:
            n['Situaçao'] = 'RAZOAVEL'
        elif m <= 5:
            n['Situaçao'] = 'RUIM'
    return n


# Programa principal
print(notas(3, 7.6, 4, 5, sit=True))
help(notas)
