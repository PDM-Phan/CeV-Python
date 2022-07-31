from time import sleep
alunos = [] # todos os alunos
boletim = [] # media dos alunos

while True:
    aluno = [] # lista com a informaçao do aluno
    aluno.append(input('Nome: '))
    aluno.append(float(input('Nota1: ')))
    aluno.append(float(input('Nota1: ')))
    boletim.append((aluno[1] + aluno[2])/2) # media das notas
    alunos.append(aluno[:])
    esc = ' '
    if esc not in 'SN':
        esc = str(input('Deseja continuar?[S/N] ')).upper().strip()
    if esc == 'N':
        break

print('\033[1;97m-=\033[m' * 20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>10}')
print('\033[1;97m-\033[m' * 30)

for pos, b in enumerate(alunos): # posiçao dos valores de alunos totais, aluno especifico, media especifica na posiçao pos
    print(f'{pos:<4}{b[0]:<10}{boletim[pos]:>10.1f}')

while True:
    print('\033[1;97m-=\033[m' * 20)
    notas = int(input('Mostrar a nota de qual aluno? (999 interrompe) '))
    if notas <= len(alunos): # se o valor digitado for dentro de len(alunos)
        print(f'Notas de {alunos[notas][0]} sao [{alunos[notas][1]}, {alunos[notas][2]}].')
        print()
    elif notas == 999: # condiçao de parada
        print('FINALIZANDO...')
        sleep(1)
        break

print('Processo Finalizado.')
