# convertendo valores/2
# ======= EX 14 ====================================
c1 = float(input('\033[94mQuantos graus celsius vc quer converter?\033[m '))
f1 = c1 * 1.8 + 32
print('\033[94mO valor de {}C corresponde a \033[1;31m{:.1f}F\033[m '.format(c1, f1))
f2 = float(input('\033[31mQuantos graus fahrenheit vc quer converter?\033[m '))
c2 = (f2 - 32) / 1.8
print('\033[31mO valor de  {}F corresponde a \033[94m{:.1f}C\033[m '.format(f2, c2))
