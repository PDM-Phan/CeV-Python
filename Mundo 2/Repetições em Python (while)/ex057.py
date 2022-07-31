'''from time import sleep
se = 'M', 'F' # sexos F e M == True

while se != 'F' or se != 'M': # enquanto se for diferente de F ou M PRINTE
    se = str(input('Qual o seu sexo? [M/F] ')).strip().upper()
    sleep(0.5)
    if se == 'F' or se == 'M': # valor for True
        print('Obrigado pela sua cooperaçao.')
        break # terminar o loop
    else: # qualquer outra coisa
        print('Por favor escreva novamente dentro dos criterios acima.')

print('Tenha um bom dia.')'''

sexo = str(input('Informe seu sexo [M/F] ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('\033[91mPor favor, digite novamente dentro dos criterios acima:\033[m ')).upper().strip()[0]

print('\033[92mObrigado pela sua cooperaçao.\033[m')
print('\033[92mSexo {} registrado com sucesso.\033[m'.format(sexo))
