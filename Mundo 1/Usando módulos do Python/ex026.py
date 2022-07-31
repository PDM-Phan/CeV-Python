frase = str(input('\033[1;31mESCREVA AGR IMEDIATAMENTE!\033[m ')).strip()
a = frase.upper().count('A')
a1 = frase.upper().find('A') + 1
au = frase.upper().rfind('A') + 1
print('\033[37mVezes q A aparece\033[m: {}'.format(a))
print('\033[37mA primeira apariçao de um A\033[m: {}'.format(a1))
print('\033[37mA sua ultima apariçao\033[m: {}'.format(au))
