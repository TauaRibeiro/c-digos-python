from random import randint
from time import sleep
from operator import itemgetter

podium = {0 : 'Primeiro lugar', 1 : 'Segundo lugar', 2 : 'Terceiro lugar', 3 : 'Quarto lugar'}

jogo = {'Jogador 1' : randint(1, 6), 'Jogador 2' : randint(1, 6), 'Jogador 3' : randint(1, 6),
        'Jogador 4' : randint(1, 6)}

ranking = dict()

print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key= itemgetter(1), reverse= True)

print(f'{'='*20}< RANKING >{'='*20}')
for p, j in enumerate(ranking):
    print(f'{podium[p]:^20}: {j[0]:^8} com {j[1]}')

        