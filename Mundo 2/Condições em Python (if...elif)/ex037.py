b = int(input('Digite um numero: '))
print('Opçoes para conversao:\n'
      '1 - Para binario\n'
      '2 - Para octal\n'
      '3 - Para hexadecimal\n')
esc = int(input('Qual voce deseja? '))
# conversao de decimal para binario
if esc == 1:
    print('O valor binario para o numero {} é {}.'.format(b, bin(b)[2:]))
# conversao de decimal para octal
elif esc == 2:
    print('O valor octal para o numero {} é {}.'.format(b, oct(b)[2:]))
# conversao de decimal para hexadecimal
elif esc == 3:
    print('O valor hexadecimal para o numero {} é {}.'.format(b, hex(b)[2:]))
else:
    print('Opçao invalida, por favor, escolha apenas os numeros oferecidos.')