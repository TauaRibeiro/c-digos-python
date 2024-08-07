from random import randrange
num = randrange(0, 11)
adi = int(input('Escolha um número: '))
pal = 1
while adi != num:
    pal += 1
    adi = int(input('Você errou, tente novamente: '))
if pal == 1:
    print('Uau, você conseguiu acertar de primeira!!')
else:
    print('Parabéns, você precisou de {} palpites para ganhar.'.format(pal))
