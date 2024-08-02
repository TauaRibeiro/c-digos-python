#A ser melhorado...
registro = list()
jogador = dict()
partidas = list()

while True:
    jogador['nome'] = input('Digite o nome: ')
    jogador['num_partidas'] = int(input(f'Digite o número de partidas jogadas por {jogador["nome"]}: '))
    jogador['total_gols'] = 0

    for x in range(0, jogador['num_partidas']):
        partidas.append(int(input(f'Quantos gols na partida {x+1}? ')))

        jogador['total_gols'] += partidas[x]

    jogador['jogos'] = partidas[:]

    registro.append(jogador.copy())

    while True:
        continuar = input('Deseja continuar? [Sim/Não]: ').lower()

        if continuar in 'simnaonão':
            break

    if continuar in 'naonão':
        break

    print('-'*30)

print('=-'*30)
print(f'{'cod'} {'nome':<15}{'gols':<17}{'total'}')
print('-'*40)
for c, j in enumerate(registro):
    print(f'{c:^3}{j["nome"]:<15}{j["jogos"]}{j["total_gols"]:>9}')
