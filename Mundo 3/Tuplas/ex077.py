palavras = ('aprender',
            'programar',
            'linguagem',
            'python',
            'curso',
            'gratis',
            'estudar',
            'praticar',
            'trabalhar',
            'mercado',
            'programador',
            'futuro')
for p in palavras: # pegar cada palavra da tupla
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p: # pegar cada palavra da tupla
        if letra.lower() in 'aeiou': # verificando so as vogais
            print(letra, end=' ') # printando elas