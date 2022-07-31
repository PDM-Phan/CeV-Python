from datetime import date
from time import sleep
print('Por favor responda algumas perguntas primeiro, antes de cadastrar no alistamento.')
sexo = str(input('\033[34mMasculino\033[m ou \033[1;35mFeminino\033[m? ')).upper().strip()
# periodo de alistamento
dado = date.today().year
# botando os dados em pratica
if sexo == 'MASCULINO':
    nascimento = int(input('\033[97mEm que ano voce nasceu?\033[m '))
    alistamento = nascimento + 18
    print('\033[37mANALIZANDO OS DADOS...\033[m')
    sleep(1)
    if dado < alistamento:
        print('\033[1;33mAinda precisara se alistar, faltando \033[4;33m{}\033[m \033[1;33mano(s)\033[m.'
              .format(alistamento - dado))
        print('O seu alistamento sera em \033[4m{}\033[m.'.format(alistamento))
    elif dado == alistamento:
        print('\033[1;92mEstá na hora de se alistar!\033[m')
    elif dado > alistamento:
        print('\033[1;91mJa passou do perido para se alistar, por \033[4;91m{}\033[m \033[1;91mano(s)\033[m.'
              .format(dado - alistamento))
        print('O seu alistamento foi em \033[4m{}\033[m.'.format(alistamento))
elif sexo == 'FEMININO':
    sleep(1)
    print('Voce nao precisa fazer o alistamento obrigatorio, deseja continuar?.')
