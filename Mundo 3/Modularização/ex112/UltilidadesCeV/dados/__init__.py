def leiadinheiro(msg=''):
    while True:
        p = input(msg).replace(',', '.').strip()
        if p.isalpha() or p == '':
            print(f'\033[31mERRO: "{p}" é um preço invalido!\033[m')
        else:
            p = float(p)
            return p
