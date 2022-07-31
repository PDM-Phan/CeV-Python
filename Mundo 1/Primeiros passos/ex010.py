#conversao de moedas
# ========= EX 10 ===============================================================
r = float(input('\033[1;34mQuantos reais vc tem na carteira?\033[m '))
d = r / 5.74
print('\033[1;34mO valor q vc pode sacar em dolar é:\033[m {:.2f}'.format(d))
if d >= 1000:
    print('\033[1;32mVAI COM DEUS PARÇA!\033[m')
else:
    print('\033[33mMelhor ficar no Brasil por enquanto kk\033[m')
