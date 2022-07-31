from datetime import date

ano = date.today().year
# separando uma lista no qual irao ficar as pessoas para seus determinados grupos
midade = []
meidade= []
for id in range(1, 8):
    nascimento = int(input('Em que ano a {} pessoa voce nasceu? '.format(id)))
    idade = ano - nascimento
# condiçoes para a divisao da lista
    if idade < 21:
        meidade.append(idade)
    elif idade >= 21:
        midade.append(idade)
# mostrando os valores
print('{} pessoas que ainda vao atingir a maior idade.'.format(len(meidade)))
print('{} pessoas que já atingiram a maior idade.'.format(len(midade)))

