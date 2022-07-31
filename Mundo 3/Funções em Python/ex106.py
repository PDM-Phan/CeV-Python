from time import sleep
# lista com todas as cores
c = ('\033[m',           # 0 - sem cor
     '\033[7;31;107m',   # 1 - vermelho
     '\033[7;32;107m',   # 2 - verde
     '\033[7;34;107m',   # 3 - azul
     '\033[7;30m'        # 4 - branco
)


def ajuda(com): # painel com as informaçoes das funçoes e bibliotecas
    titulo(f'Acessando o manual de comando \'{com}\'', 3)
    print(c[4], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0): # painel com o titulo dos paineis
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('\033[mFunçao ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO', 1)