soma = 0
cont = 0

for p in range(1, 7):
    num = int(input('Digite o {} numero inteiro: '.format(p)))
    if num % 2 == 0: # determinando numeros pares
        soma = soma + num # somando todos os numeros pares
        cont = cont + 1 # quantidade de numeros pares

print('A soma de {} numero(s) par(es) é: {}'.format(cont, soma))
print('Todos os numeros impares foram desconsiderados.')

