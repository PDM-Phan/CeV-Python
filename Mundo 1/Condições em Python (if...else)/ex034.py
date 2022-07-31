sal = float(input('O salario para um funcionario na empresa X é '))
if sal > 1250:
    nsal = sal * 1.10
    aumento = nsal - sal
    print('O valor do aumento é: \033[33m{:.2f}\033[m reais'.format(aumento))
    print('Recebendo agr: \033[32m{:.2f}\033[m reais'.format(nsal))
else:
    nsal1 = sal * 1.15
    aumento1 = nsal1 - sal
    print('O valor do aumento é: \033[33m{:.2f}\033[m reais'.format(aumento1))
    print('Recebendo agr: \033[32m{:.2f}\033[m reais'.format(nsal1))
