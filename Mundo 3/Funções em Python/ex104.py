def leiaint(msg):
   while True:
       num = str(input(msg))
       if num.isnumeric():
           num = int(num)
           return num
       else:
           print('\033[91mERRO! Digite um numero interio valido.\033[m')


#Programa principal
num = leiaint('Digite um numero: ')
print(f'Voce acabou de digitar um numero {num}.')
