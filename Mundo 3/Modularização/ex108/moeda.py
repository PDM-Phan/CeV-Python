def metade(p):
    res = p / 2
    return res


def dobro(p):
    res = p * 2
    return res


def aumento(p, a):
    res = p + (p * (a/100))
    return res


def diminuir(p, d):
    res = p - (p * (d/100))
    return res

def moeda(p = 0, taxa = 'R$'):
    return f'{taxa}{p:.2f}'.replace('.', ',')
