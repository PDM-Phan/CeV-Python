from time import sleep
# compra de um produto aleatorio kk
compra = float(input('Opçoes de pagamento para a compra de UMA \033[1;93mBEYBLADE\033[m por \033[32mR$\033[m'))
op = int(input('Digite: \n'
               '1 - Para \033[1;34mÀ VISTA EM DINHEIRO\033[m\n'
               '2 - Para \033[1;34mÀ VISTA EM CARTAO\033[m\n'
               '3 - Em até \033[1;34m2x NO CARTAO\033[m\n'
               '4 - Em \033[1;34m3x OU MAIS NO CARTAO\033[m\n'
               'Opção: '))
sleep(1)
# opçoes de pagamento
if op == 1:
    vdes = compra * 0.90
    print('O valor a ser pago será, \033[1;32mR${:.2f}\033[m, apos receber \033[1;34m10% de desconto\033[m.'.format(vdes))
elif op == 2:
    vdes = compra * 0.95
    print('O valor a ser pago será, \033[1;32mR${:.2f}\033[m, apos receber \033[1;34m5% de desconto\033[m.'.format(vdes))
elif op == 3:
    v = compra / 2
    print('O valor a ser pago é \033[4;32mR${:.2f}\033[m em 2 parcelas de \033[1;32mR${:.2f}\033[m.'.format(compra, v))
elif op == 4:
    vt = compra * 1.20
    parcelas = int(input('Em quantas parcelas? '))
    par = vt / parcelas
    print('Com parcelas de \033[4;31mR${:.2f} COM JUROS\033[m,'
          ' indo de \033[4;32mR${:.2f}\033[m para \033[1;31mR${:.2f}\033[m,\n'
          'Por conta dos \033[1;91m20% de juros totais\033[m.'.format(par, compra, vt))
else:
    print('\033[1;91m==========\!!!ERROR!!!\================\033[m')
    sleep(1)
    print('\033[1;91m!!WARNING!!\033[m\n' * 50)
