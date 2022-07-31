# cauculo de area
# ======== EX 11 =================================================================
h = float(input('\033[1;37mQuantos metros de altura essa parede tem?\033[m '))
la = float(input('\033[1;37mQuantos metros de largura essa parede tem? '))
a = h * la
t = a / 2
print(f'\033[1;37mA area total de uma parede q possui \033[97m{h}m\033[1;37m de altura e '
      f'\033[97m{la}m\033[1;37m de largura, é '
      f'\033[97m{a}\033[1;37m,\033[m')
print('\033[1;37mlevando em considereçao q 1l de tinta cobre 2m, serao necessarios '
      '\033[97m{}l\033[1;37m de tinta.\033[m '.format(t))
