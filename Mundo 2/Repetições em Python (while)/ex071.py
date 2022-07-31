print('=' * 30)
print('{:^30}'.format('BANCO DO DEUZAO'))
print('=' * 30)
saque = int(input('Quantos R$ voce deseja sacar? '))
ced50 = ced20 = ced10 = ced01 = 0 # quantidade de cedulas
while True:
    if saque // 50 != 0: # caso seja divisivel por 50
        ced50 = saque // 50 # calcular a quantidade de cedulas
        resto = saque % 50
        saque = resto # alterar o valor do saque para caucular outras possiveis trocas
        print('total de {} cedulas de R$50,00.'.format(ced50))
    elif saque // 20 != 0: # caso seja divisivel por 20
        ced20 = saque // 20 # calcular a quantidade de cedulas
        resto = saque % 20
        saque = resto # altear o valor de saque
        print('total de {} cedulas de R$20,00.'.format(ced20))
    elif saque // 10 != 0: # caso seja divivisivel por 10
        ced10 = saque // 10 # calcular a quantidade de cedulas
        resto = saque % 10
        saque = resto # alterar valor de saque
        print('total de {} cedulas de R$10,00.'.format(ced10))
    elif saque // 1 != 0: # se for divisivel por 1
        ced01 = saque // 1 # calculaar a quantidade de cedulas
        resto = saque % 1
        print('total de {} cedulas de R$1,00.'.format(ced01))
    if resto == 0: # condiçao de parada
        break
print('=' * 30)
print('Volte sempre!')