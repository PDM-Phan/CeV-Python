from time import sleep
n1 = int(input('\033[92mDigite um numero\033[m: '))
n2 = int(input('\033[92mDigite, mais um numero por obséquio majestade\033[m: '))
n3 = int(input('\033[92mEstou aqui novamente para pedir q digite um numero\033[m: '))
# Verificando o maior numero
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
# Verificando o menor numero
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
sleep(1)
print('\033[1;37mO maior numero foi\033[m: \033[4m{}\033[m'.format(maior))
print('\033[1;37mO maior numero foi\033[m: \033[4m{}\033[m'.format(menor))
