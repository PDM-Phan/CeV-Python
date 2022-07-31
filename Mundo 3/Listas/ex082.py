# lista = []
# listapar = []
# listaimpar = []
# while True:
#
#     num = int(input('Digite um valor: '))
#     lista.append(num) # adiciona qualquer numero digitado
#     if num % 2 == 0:
#         listapar.append(num) # adiciona somente os pares
#
#     elif num % 2 == 1:
#         listaimpar.append(num) # adiciona somente os impares
#
#     esc = input('Deseja continuar?[S/N] ').upper().strip()
#     while esc not in 'SN':
#         print('Por favor escreva somente o necessario... ')
#         esc = input('Deseja continuar?[S/N] ').upper().strip()
#     if esc == 'N':
#         break
#
# print('-=' * 20)
# print(f'A lista completa é {lista}.')
# print(f'A lista com apenas os pares é {listapar}.')
# print(f'A lista com apenas os impares é {listaimpar}.')
lista = [] # lista geral
while True:

    lista.append(int(input('Digite um valor: '))) # adcionando valores para um lista
    esc = input('Deseja continuar?[S/N] ').upper().strip()
    while esc not in 'SN':
        print('Por favor escreva somente o necessario... ')
        esc = input('Deseja continuar?[S/N] ').upper().strip()
    if esc == 'N':
        break

listapar = [] # lista apenas com os pares
listaimpar = [] # lista apenas com os impares

for n in range(0, len(lista)):
    if lista[n] % 2 == 0:
        listapar.append(lista[n]) # adcionando os valores pares na lista
    elif lista[n] % 2 == 1:
        listaimpar.append(lista[n]) # adcionando os valores impares na lista
print('-=' * 20)
print(f'A lista que foi digitada é {lista}.')
print(f'A lista apenas com os valores pares sera {listapar}.')
print(f'A lista apenas com os valores impares sera {listaimpar}.')