from time import sleep
# convertendo valores
# ========== EX 8 ==========================================================
m = float(input('\033[1;37mEm quantos metros vc esta pensando?\033[m '))
dm = m * 10
c = m * 100
mm = m * 1000
k = m / 1000
hm = m / 100
dam = m / 10
# print('A conversao de {}, para centimetros e para milimetros sao, respectivamente {} e {}.'.format(m, c, mi))
# print(f'A conversao de {m}, para centimetros e para milimetros sao, respectivamente {c} e {mi}')
# print('E se vc quiser saber quantos kilometros seria, bem, ai esta :{}'.format(k)
print('ANALIZANDO...')
sleep(1)
print(f'\033[1;37mConvertendo esse valor para outra medidas sera\033[m: \n{k}km\n{hm}hm\n{dam}dam\n{dm}dm\n{c}cm\n{mm}mm')
