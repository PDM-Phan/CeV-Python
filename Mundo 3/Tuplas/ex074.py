from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10) # 5 numeros aleatorios numa tupla
    , randint(1, 10), randint(1, 10))
print('Os numeros sorteados foram: ', end='')

for n in num:
    print(n, end=' ')

# nums = sorted(num) # colocando os numeros da tupla em ordem
print(f'\nO maior numero sorteado foi {max(num)}.') # pegando o maior valor
print(f'O menor numero sorteado foi {min(num)}.') # pegando o menor valor
