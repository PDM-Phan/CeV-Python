valor = int(input('\033[1;33mDigite um numero que voce queira saber de sua tabuada:\033[m '))
print('\033[1;33m-=\033[m' * 30)
for t in range(1, 11):
    total = valor * t
    print(f'{valor} x {t} = {total}')
print('\033[1;33m-=\033[m' * 30)
print('Pronto.')