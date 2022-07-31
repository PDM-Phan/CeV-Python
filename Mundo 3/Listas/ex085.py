numeros = [[], []]

for n in range(1, 8):
    num = int(input(f'Digite o valor do {n} numero: '))
    if num % 2 == 0:
        numeros[0].append(num) # se o numero for par, colocado na lista 0
    else:
        numeros[1].append(num) # se o numero for impar, colocado na lista 1

print('-=' * 20)
# colocando as listas em ordem crescente
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores impares digitados foram: {numeros[1]}')