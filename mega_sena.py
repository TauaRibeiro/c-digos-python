from random import randint
from time import sleep

resultado = list()
palpite = list()

print('-'*50)
print('{:^50}'.format('SIMULADOR MEGA SENA'))
print('-'*50)

quantidade = int(input('Digite o número de palpites que deseja gerar: '))
print('='*15, end='  ')
print('SIMULANDO {} {}'.format(quantidade, 'PALPITES' if quantidade > 1 else 'PALPITE'), end= '  ')
print('='*15)


for x in range(0, quantidade):
    for y in range(0, 6):
        num = randint(1, 60)

        while num in palpite:
            num = randint(1, 60)
        
        palpite.append(num)


    resultado.append(palpite[:])
    palpite.clear()

for p in range(0, quantidade):
    print(f'Palpite {p+1}: {resultado[p]}')

    sleep(1)

print('='*20, end= ' <')
print(' BOA SORTE! ', end= '> ')
print('='*20)
