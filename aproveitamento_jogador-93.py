registro = list()
jogador = dict()
partidas = list()

maior_placar = 0
while True:
    jogador['nome'] = input('Digite o nome: ')
    numero_partidas = int(input(f'Digite o número de partidas jogadas por {jogador["nome"]}: '))
    jogador['total_gols'] = 0

    for x in range(0, numero_partidas):
        partidas.append(int(input(f'Quantos gols na partida {x+1}? ')))

        jogador['total_gols'] += partidas[x]

    jogador['jogos'] = partidas[:]
    partidas.clear()

    if maior_placar == 0 or len(jogador['jogos']) > maior_placar:
        maior_placar = len(jogador['jogos'])

    registro.append(jogador.copy())
    
    jogador.clear()

    while True:
        continuar = input('Deseja continuar? [Sim/Não]: ').lower()

        if continuar in 'simnaonão':
            break

    if continuar in 'naonão':
        break

    print('-'*30)
print('=-'*30)
print(f'{'cod':<9}{'nome':<12}{'total':<15}{'gols'}')
print('-'*40)


for c, j in enumerate(registro):
    print(f'{c:<9}', end='')
    for v in j.values():                     
        print(f'{str(v):<13}', end='')
    print()
    
while True:
    while True:
        escolha = int(input('Mostrar dados de qual jogador [999 finaliza]? '))

        if escolha < len(registro) and escolha >= 0 or escolha == 999:
            break
        
        print('Escolha inválida!! Tente novamente...')
    
    if escolha == 999:
        break

    print(f'--LEVANTAMENTO DO JOGADOR {registro[escolha]["nome"]}:')
    for j, g in enumerate(registro[escolha]["jogos"]):
        print(f'  No jogo {j+1} fez {g} {"gol" if g == 1 else "gols"}.')

    print('-'*50)


print('<< VOLTE SEMPRE >>')