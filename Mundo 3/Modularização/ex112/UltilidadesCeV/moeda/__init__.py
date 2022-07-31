def metade(p=0, m=False):
    res = p / 2
    if m:
        return moeda(res)
    else:
        return res


def dobro(p=0, m=False):
    res = p * 2
    if m:
        return moeda(res)
    else:
        return res


def aumento(p=0, a=0, m=False):
    res = p + (p * (a/100))
    if m:
        return moeda(res)
    else:
        return res


def diminuir(p=0, d=0, m=False):
    res = p - (p * (d/100))
    if m:
        return moeda(res)
    else:
        return res

def moeda(p=0, taxa='R$'):
    return f'{taxa}{p:.2f}'.replace('.', ',')

def resumo(p=0, a=10, d=5):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analizado:":<20}{moeda(p):<20}')
    print(f'{"Dobro do preço:":<20}{dobro(p, True):<20}')
    print(f'{"Metade do preço:":<20}{metade(p, True):<20}')
    print(f'{f"{a}% de aumento:":<20}{aumento(p, a, True):<20}')
    print(f'{f"{d}% de reduçao:":<20}{diminuir(p, d, True):<20}')
    print('-' * 30)
