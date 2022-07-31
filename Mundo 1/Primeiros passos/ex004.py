# caracteristicas de algo digitado
#====== EX 4 ============================================================================================================
algo = str(input('\033[32mDigite alguma coisa ai por favor, bença\033[m:'))
print('\033[34mAqui vai o tipo do que vc escreveu\033[m!')
print(type(algo))
print('\033[1;31mAgora pra mostrar que não estamos brincando com o serviço, aqui vai outras coisas q vc n sabia que nós sabiamos\033[m!')
print(f'{algo}, \033[37mpossui apenas números?\033[m ', algo.isnumeric())
print(f'{algo}, \033[37mpossui apenas palavras?\033[m', algo.isalpha())
print(f'{algo}, \033[37mé uma possui alguma das duas opções acima?\033[m', algo.isalnum())
print(f'{algo}, \033[37mé composta(o) apenas por letras maiúsculas?\033[m', algo.isupper())
print(f'{algo}, \033[37mé composta(o) apenas por letras minúsculas?\033[m', algo.islower())
print(f'{algo}, \033[37mestá capitalizada?\033[m', algo.istitle())
print(f'{algo}, \033[37msó tem espaços?\033[m', algo.isspace())

