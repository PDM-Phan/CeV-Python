n = 0 # soma
cont = 0 # contador de numeros
for c in range(1, 501, 2): # arranjo
     if c % 3 == 0: # separar numeros impares q sao multiplos de 3
        cont = cont + 1 # contando os componentes
        n = n + c # soma entre eles
print('O somatorio entre os \033[3;34m{}\033[m'
      ' numeros impares multiplos de \033[4;33m3\033[m é \033[4;32m{}\033[m'.format(cont, n))
