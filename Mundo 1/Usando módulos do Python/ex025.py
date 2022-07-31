print('\033[32mBoa noite, estamos realizando uma pesquisa pra saber quantos pobres tem no brasil, poderia nos ajudar?\033[m ')
no = str(input('\033[32mQual seu nome?\033[m ')).strip()
p = no.upper().find('SILVA')
if p == -1:
    print('\033[36mPARABENS!, voce nao é pobre!\033[m')
else:
    print('\033[31mInfelizmente vc ... :(\033[m')
