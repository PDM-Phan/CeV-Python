n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
# cauculando media e resultados
if m <= 5:
    print('Por ter tirando \033[4;91m{}\033[m, o aluno será \033[1;91mREPROVADO\033[m na materia.'.format(m))
elif 5 < m <= 6.9:
    print('Por ter tirado \033[4;93m{}\033[m, o aluno estará de \033[1;93mRECUPERAÇAO\033[m na materia.'.format(m))
elif m >= 7:
    print('Por ter tirado \033[4;92m{}\033[m, o aluno será \033[1;92mAPROVADO\033[m na materia.'.format(m))