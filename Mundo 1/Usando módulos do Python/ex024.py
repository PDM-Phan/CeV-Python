print('\033[32mEstamos juntando as pessoas que moram em cidades que começem com SANTO, voce poderia nos ajudar?\033[m')
cidade = str(input('\033[32mOnde voce mora?\033[m ')).strip()
a = cidade.upper().find('SANTO')
if a == 0:
    print('\033[36mPelo visto vc mora em uma cidade dos parametros, obg pela sua cooperaçao.\033[m')
else:
    print('\033[31mInfelizmente vc n mora em uma cidade q começe com SANTO. Obg pela cooperaçao.\033[m')
