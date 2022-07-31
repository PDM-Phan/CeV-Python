print('=' * 50)
print('1O TERMOS DE UMA \033[1;97mP.A\033[m DE SUA ESCOLHA!')
print('=' * 50)

n1 = int(input('Primeiro termo da P.A: '))
r = int(input('Razao da P.A: '))
decimo = n1 + (10 - 1) * r # como caucular o 10 termo da P.A

for pa in range(n1, decimo + r, r): # decimo + r = ir para o proximo numero da P.A
    print('{}'.format(pa), end=' -> ') # realizando a razao
print('Acabou!')
