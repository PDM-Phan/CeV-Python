from time import sleep
print('Para realizar um emprestimo, antes precisamos saber de algumas coisas:')
casa = float(input('Valor da casa desejada: '))
salario = float(input('Qual o seu salario? '))
prest = int(input('Em quantos anos se deseja pagar? '))
# dividindo o ano para mes
prestme = prest * 12
# cauculando o valor das prestaçoes por mes
vprestme = casa / prestme
sleep(1)
if vprestme <= salario * 0.30:
    print('\033[1;32mO valor do emprestimo foi aprovado!\033[m')
elif vprestme > salario * 0.30:
    print('\033[1;31mInfelizmente n sera possivel realizar o emprestimo.\033[m')