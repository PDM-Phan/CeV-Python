n1 = int(input('\033[1;34mDigite um numero inteiro\033[m: '))
n2 = int(input('\033[1;33mDigite outro numero inteiro\033[m: '))
# comparando os numeros
if n1 > n2:
    print('\033[34mO primeiro numero é maior\033[m.')
elif n2 > n1:
    print('\033[33mO segundo numero é maior\033[m.')
else:
#elif n1 == n2:
    print('\033[36mNao há numero maior, pois, ambos sao iguais\033[m.')