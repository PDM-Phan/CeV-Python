# soluçao de UVA - SAMA
'''num = int(input('Digite um numero: '))
rnum = int(num ** (1/2))
primo = True # booleano, tratando primo = true

for x in range(2, rnum + 1): # teste do numero
    if num % x == 0:
        print('Nao é primo.')
        primo = False
        break # força a parada do for

if primo:
    print('sim')'''
# OBS; numeros primos so sao divididos 2 vezes.
# soluçao Guanabara:

num = int(input('Digite um numero: '))
tot = 0 # "booleano"
# checando se é primo.

for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
        if tot > 2: # mostrando que nao é primo..
            print('Nao é primo, pois foi dividido mais de 2 vezes.')
            break
if tot == 2: # se for primo
    print('Sim, é primo.')
