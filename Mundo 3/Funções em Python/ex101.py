def voto(nasc):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - nasc
    print(f'Com {idade}: ', end='')
    if idade >= 65 or 16 >= idade < 18:
        return print('VOTO OPCIONAL.')
    elif idade >= 18:
        return print('VOTO OBRIGATORIO.')
    elif idade < 16:
        return print('NAO VOTA.')


# Programa principal
print('-' * 30)
nasc = int(input('Em que ano voce nasceu? '))
voto(nasc)