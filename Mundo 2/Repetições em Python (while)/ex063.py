# n = int(input('Digite um numero inteiro: '))
# count = 0 # contador
# fib2 = 0
# fib1 = 0
#
# while count < n:
#     resultado = fib1 + fib2 # realiza a soma entre os dois numeros
#     if resultado == 0: # fibonnaci sempre sera igual a zero ate adcionar 1
#         resultado += 1 # adicionando 1
#     fib2 = fib1 # passa o 2 valor para o 1
#     fib1 = resultado # o resultado da soma se torna o primeiro valor
#     print(resultado, end=' ')
#     count += 1 # contador
f = int(input('Quantidade de termos da sequencia: '))
t1 = 0 # primeiro termo da sequencia
t2 = 1 # segundo termo da sequencia
print('{} -> {}'.format(t1, t2), end='')
count = 3 # contador começara a partir do 3 termo, pois os dois primeiros ja foram printados

while count <= f:
    t3 = t1 + t2 # terceiro termo
    print(' -> {}'.format(t3), end='')
    # troca de posiçoes/valores
    t1 = t2
    t2 = t3
    count += 1

print(' -> Apenas!')
