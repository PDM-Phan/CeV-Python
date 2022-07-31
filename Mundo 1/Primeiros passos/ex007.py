# tirando a media de um aluno
# ============ EX 7 =======================================================
n1 = float(input('\033[1;32mDigite, de 0-10, a primeira nota de um aluno\033[m: '))
n2 = float(input('\033[1;34mDigite, de 0-10,  a segunda nota de um aluno\033[m: '))
m = (n1 + n2)/2
# print('A media em uma materia para um aluno q tirou, {} na primeira prova e {} na segunda prova é {}.'.format(n1,
# n2, m))
print(f'\033[1;33mA media em uma materia para um aluno q tirou, \033[4;30m{n1}\033[m\033[1;33m na primeira prova e '
      f'\033[4;30m{n2}\033[m\033[1;33m na segunda prova é \033[4;30m{m}\033[m.')
if m >= 7:
    print('\033[1;36mPARABENS, ELE FOI APROVADO!\033[m')
else:
    print('\033[1;31mInfelizmente, ele foi reprovado...\033[m')