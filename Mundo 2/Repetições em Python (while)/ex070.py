from time import sleep

soma = 0
pro1000 = 0
barato = 0
probarato = ' ' # nome do produto mais barato
cont = 0 # contador apenas para usar uma condiçao
print('\033[1;93m==============LOJINHA DO DEUS==============\033[m')

while True:
    pro = str(input('\033[1;93mQual o nome do produto que voce comprar?\033[m ')).strip().capitalize()
    valor = float(input('\033[92mR$:\033[m '))
    sleep(1)
    print('-=' * 20)
    cont += 1
    soma += valor
    if valor >= 1000:
        pro1000 += 1
    if cont == 1 or valor < barato: # condiçao para descobrir o produto mais barato
        probarato = pro
        barato = valor
    # else:
    #     if valor < barato:
    #         probarato = pro
    dec = ' '
    while dec not in 'SN':
        dec = str(input('Deseja realizar outra compra?[\033[94mS\033[m/\033[91mN\033[m] ')).strip().upper()
    if dec == 'N':
        break
    sleep(1)
    print('-=' * 20)
print('-=' * 20)
print('\033[1;37mFinalizando a(s) compras...\033[m')
sleep(1)
print('O valor total da compra foi de \033[92mR${}\033[m.'.format(soma))
print('-' * 40)
print('{} dos produtos comprados custam mais de \033[92mR$1000,00\033[m.'.format(pro1000))
print('-' *  40)
print('O nome do produto mais barato foi \033[36m{}\033[m'.format(probarato))
