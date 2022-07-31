#cauculando um custo de uma viagem baseado no km
print('\033[92mBom dia, se voce esta aqui é pq pretende realizar uma viagem e quer saber quanto ela le custara, mas antes, '
      'precisamos saber uma coisa\033[m:')
via = float(input('\033[1;92mQuantos kilomentos voce pretende viajar\033[m? '))
if via <= 200:
    custo = via * 0.50
    print('O custo para realizar uma viagem de {}km sera {} reais.'.format(via, custo))
else:
    custo2 = via * 0.45
    print('O custo para realizar uma viagem de {}km sera {} reais.'.format(via, custo2))
print('\033[92mTenha uma boa viagem\033[m!')