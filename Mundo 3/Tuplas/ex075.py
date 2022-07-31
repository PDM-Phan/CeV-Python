val = (int(input('Digite um numero: ')), int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')), int(input('Digite o ultimo numero: ')))
print(f'Os numeros que voce digitou foram: {val}.')
print(f'O valor 9 apareceu {val.count(9)} vez(es).') # contando a quantidade de apariçoes do valor 9
# colocar o if para nao haver erro durante o codigo
if 3 in val: # caso seja digitado o valor 3
    print(f'A posiçao do valor 3 apareceu na {val.index(3) + 1} posiçao.')
else: # caso nao seja digitado
    print('Voce nao digitou nenhum numero 3.')
print('Os numeros pares que foram digitados foram  ', end='')
for p in val:
    if p % 2 == 0: # determinar o se o valor é par dentro da tupla
        print(p, end=' ')
