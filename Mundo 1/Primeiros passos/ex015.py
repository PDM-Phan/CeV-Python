from time import sleep
# cauculando o custo de uma viagem
# ======= EX 15 ======================================
km = float(input('Quantos km voce rodou com o seu carro? '))
dia = int(input('A quantos dias faz desde que vc alugou o carro? '))
aldia = 60 * dia
alkm = 0.15 * km
altotal = aldia + alkm
print('Cauculando valor....')
sleep(1)
print('O valor total a se pagar no aluguel do carro sera: \033[1;32mRS{}\033[m'.format(altotal))
