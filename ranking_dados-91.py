#A ser terminado
from random import randint
from time import sleep

posicao = {1:'Primeiro', 2:'Segundo', 3:'Terceiro', 4:'Quarto'}
ranking = dict()
organizar = [[], [], [], []]

for x in range(1, 5):
    organizar[x-1].append(x)
    organizar[x-1].append(randint(1, 6))

    for y in range(1, x):
        if organizar[y-1][1] > organizar[x-1][1]:

        


        