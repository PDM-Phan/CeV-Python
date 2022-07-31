from datetime import date
anoa = date.today().year
anna = int(input('Em que ano voce nasceu? '))
idade = anoa - anna
# determinando categoria
if idade <= 9:
    print('Por ter {} anos, voce pertencerá a categoria \033[1;34mMIRIM\033[m.'.format(idade))
elif idade <= 14:
    print('Por ter {} anos, voce pertencerá a categoria \033[1;34mINFANTIL\033[m.'.format(idade))
elif idade <= 19:
    print('Por ter {} anos, voce pertencerá a categoria \033[1;34mJUNIOR\033[m.'.format(idade))
elif idade <= 25:
    print('Por ter {} anos, voce pertencerá a categoria \033[1;34mSENIOR\033[m.'.format(idade))
elif idade > 25:
    print('Por ter mais que 20 anos, voce pertencerá a categoria \033[1;34mMASTER\033[m.')
