def ficha(nome, numero_gols):
    if nome.isalnum() == False:
        nome = '< desconhecido >'
    if numero_gols.isnumeric() == False:
        numero_gols = 0 

    print(f'O jogador {nome} fez {numero_gols} {"gol" if numero_gols == 1 else "gols"} no campeonato.')

ficha(input('Digite o nome do jogador: '), input('Digite o número de gols: '))