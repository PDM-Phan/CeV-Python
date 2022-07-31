#separando nomes
ncom = str(input('\033[92mDigite seu nome completo agr, imediatamente pf\033[m: ')).title().strip()
nco = ncom.split()
print('\033[92mPrimeiro nome\033[m: \033[1;33m{}\033[m'.format(nco[0]))
print('\033[92mUltimo nome\033[m: \033[34m{}\033[m'.format(nco[-1]))