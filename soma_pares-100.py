from random import randint
from time import sleep


numeros = list()


def sorteio(numeros):
    print('Sorteando 5 valores da lista: ', end='')
    for x in range(0, 5):
        numeros.append(randint(0, 9))

        print(numeros[x], end=' ', flush= True)
        sleep(0.5)
    
    print('PRONTO!!')


def somaPares(numeros):
    total = 0

    for numero in numeros:
        if numero % 2 == 0:
            total += numero

    print(f'Somando os valores pares de {numeros}, temos {total}')


sorteio(numeros)

somaPares(numeros)