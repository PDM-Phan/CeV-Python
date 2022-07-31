def escreva(msg):
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))


escreva('Gustavo Guanabara')
escreva('Curso em Python no Youtube')
escreva('CeV')
print('Agora é a sua vez de alterar a frase!')
escreva(input('O que voce quer escrever? '))
