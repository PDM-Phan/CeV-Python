# testando novas funçoes: diferentemente dos exercicios anteriores!!!
nome = str(input('\033[32mDigite seu nome completo aqui do lado, bença >\033[m ')).strip()
print('\033[31mAgr vamos brincar com ele >:)\033[m')
print('\033[37mComposto apenas por letras maiusculas\033[m:', nome.upper())
print('\033[37mComposto apenas por letras minusculas\033[m:', nome.lower())
nome2 = nome.split()
print('\033[37mQuantidade de letras\033[m:', len((''.join(nome2))))
print('\033[37mQuantidade de letras de apenas o seu primeiro nome\033[m:', len(nome2[0]))
