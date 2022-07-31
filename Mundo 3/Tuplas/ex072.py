# guardando os nomes dos numeros de 0 a 20.
nex = ('zero', 'um', 'dois', 'trêS', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze'
       , 'quatorse', 'quinze', 'dizesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
esc = ' '
while esc != 'N':
    while True:
        num = int(input('Digite um numero de 0 - 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Voce digitou o numero {nex[num]}') # colocar por extenso o numero digitado
    esc = str(input('Deseja digitar outro numero?[S/N] ')).upper().strip()

