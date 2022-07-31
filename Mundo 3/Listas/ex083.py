expressao = [] # expressao

ex = str(input('Escreva uma expressao que use parenteses: ')) # conteudo da expressao

for e in range(0, len(ex)):
    expressao.append(ex[e]) # adicionando cada contedudo da expressao separadamente

if expressao.count('(') == expressao.count(')'): # verificando se quantidade de parenteses abertos sao iguais a de parenteses fechados
    print('Sua expresssao esta válida.')
else:
    print('Sua expressao esta inválida.')
