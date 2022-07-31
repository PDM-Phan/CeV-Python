# import random
# carroloko = random.randint(40, 200)
print('\033[33mUm carro esta passando por uma lombada eletronica com limite de 80km/h\033[m,')
vel = int(input('\033[33mA velocidade atingida pelo carro foi\033[m: '))
velex = vel - 80
multa = 7 * velex
if vel > 80:
    print(
        '\033[31mAtingindo \033[4;31m{}km/h\033[m\033[31m, assim ultrapassando a velocidade permitida por '
        '\033[4;31m{}km/h\033[m\033[31m a multa sera de\033[m: {} reais '.format(vel, velex, multa))
    # print('Atingindo {}, assim ultrapassando a velocidade permitida por {} a multa sera de: {} reais'.format(carroloko, velex, multa))

else:
    print('\033[32mAtingindo \033[4;32m{}km/h\033[m'
          '\033[32m, nao infringindo o limite de velocidade, nao havera nenhuma multa\033[m.'.format(vel))
    # print('Atingindo {}, nao infringindo o limite de velocidade, nao havera nenhuma multa.'.format(carroloko))
