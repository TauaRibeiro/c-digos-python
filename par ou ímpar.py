from random import randrange
from time import sleep
print('=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('VAMOS JOGAR PAR OU ÍMPAR')
vitoria = 0
decisao = ' '
while True:
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-')
    num = int(input('Digite um valor: '))
    while decisao not in 'pi':
        decisao = input('Par ou Ímpar? [P/I] ').lower()
    num2 = randrange(0, 11)
    print('-----------------------')
    print(f'Você jogou {num} e o computador jogou {num2}. Total de {num+num2}', end=' ')
    print('DEU PAR' if (num + num2) % 2 == 0 else 'DEU ÍMPAR')
    print('-----------------------')
    sleep(1)
    if decisao == 'p' and (num + num2) % 2 == 0:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        vitoria += 1
        sleep(1)
    elif decisao == 'i' and (num + num2) % 2 != 0:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        vitoria += 1
        sleep(1)
    else:
        print('Você PERDEU')
        sleep(1)
        break
print(f'GAME OVER! Você venceu {vitoria} vezes.')
