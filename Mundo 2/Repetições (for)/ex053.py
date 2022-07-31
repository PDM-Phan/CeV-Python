f = str(input('Escreva uma frase: ')).split() # frase separada
fj = ''.join(f).lower() # frase em minuscula
fi = fj[::-1] # frase invertida
print('O inverso de {} é {}.'.format(fj, fi))

if fi == fj: # comparaçao
    print('Essa frase é um PALINDROMO.')
else:
    print('Essa frase nao é um PALINDROMO.')
