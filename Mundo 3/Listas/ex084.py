from time import sleep
pessoas = [] # lista com todas as pessoas
maior = menor = 0
while True:
    pessoa = [] # lista de cada pessoa
    pessoa.append(str(input('Nome: ')).strip())
    pessoa.append(float(input('Peso: ')))
    print('-' * 25)
    pessoas.append(pessoa[:]) # cria uma copia de pessoa, e adiciona em pessoas
    if len(pessoas) == 1: # se for a primeira pessoa, o menor e o menor peso sera dela
        menor = pessoa[1]
        maior = pessoa[1]
    else:
        if pessoa[1] >= maior: # se o peso da proxima pessoa for maior
            maior = pessoa[1]
        elif pessoa[1] <= menor: # se o peso da proxima pessoa for menor
            menor = pessoa[1]
    esc = ' '
    if esc not in 'NS':
        esc = str(input('Deseja continuar?[S/N] ')).strip().upper()
    if esc == 'N':
        break
    print('-' * 25)

print('Cadastrando...')
print('-=' * 30)
sleep(1)
print(f'Ao todo foram cadastrados {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior}Kg e foram  de ', end= '')
for p in pessoas:
    if p[1] == maior: # verificando se o peso de cada pessoa é igual ao maior
        print(f'{p[0]}... ', end='')

print(f'\nO menor peso foi {menor}Kg e foram de ', end='')
for p in pessoas:
    if p[1] == menor: # verificando se o peso de cada pessoa é igual ao menor
        print(f'{p[0]}... ', end='')
