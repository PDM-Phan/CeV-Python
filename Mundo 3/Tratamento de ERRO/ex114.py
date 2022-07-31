import urllib.request

try:
    site =  urllib.request.urlopen('http://www.pudim.com.br/') # verificar se o site esta acessivel
except:
    print('ERRO: O site PUDIM esta indisponivel no momento.')
else:
    print('O site PUDIM esta acessivel no momento.')
