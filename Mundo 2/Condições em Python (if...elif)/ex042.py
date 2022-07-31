print('Quer saber seu IMC?')
altura = float(input('Qual sua altura? '))
peso = float(input('Qual seu peso? '))
imc = peso / (altura ** 2)
# cauculando o imc
if imc <= 18.5:
    print('Por possuir \033[4;34m{:.1f}\033[m, sendo assim, '
          'abaixo de 18.5, voce esta \033[4;34mABAIXO DO SEU PESO IDEAL\033[m.'.format(imc))
elif 18.5 <= imc < 25:
    print('Por possuir \033[4;34m{:.1f}\033[m, '
          'estando entre 18.5 e 25, voce esta \033[1;34mNO SEU PESO IDEAL\033[m.'.format(imc))
elif 25 <= imc < 30:
    print('Por possuir \033[4;34m{:.1f}\033[m, estando entre 25 e 30, voce esta \033[1;34SOBREPESO\033[m.'.format(imc))
elif 30 <= imc < 40:
    print('Por possuir \033[4;34m{:.1f}\033[m, estando estre 30 e 40, voce esta \033[1;34mOBESO\033[m.'.format(imc))
else:
    print('Por possuir mais de 40, voce ta \033[1;91mMORRENDO\033[m.')
