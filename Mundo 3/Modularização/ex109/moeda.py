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
