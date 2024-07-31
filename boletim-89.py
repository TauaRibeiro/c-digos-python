from time import sleep

boletim = list()
dados = list()

qtd_cadastros = 0

while True:
    dados.append(input('Digite o nome do aluno: '))
    dados.append(float(input('Digite a primeira nota: ')))
    dados.append(float(input('Digite a segunda nota: ')))
    dados.append((dados[1]+dados[2])/2)

    boletim.append(dados[:])
    dados.clear()

    qtd_cadastros += 1

    while True:
        continuar = input('Deseja continuar? [Sim/Não]: ').lower()

        if continuar in 'simnãonao':
            break
        
        print('Opção inválida!! Tente novamente...\n')
    
    if continuar in 'nãonao':
        break

while True:
    print('='*30)
    print('{:-<10}{:-<20}{}'.format('NÚMERO', 'NOME', 'MÉDIA'))
    for x in range(0, qtd_cadastros):
        print('{:<10}{}{}{}'.format(x, boletim[x][0], ' '*(20 - len(boletim[x][0])), boletim[x][3]))
    print('='*30)
    
    aluno = int(input('Digite o número do aluno que deseja consultar o boletim [999 termina o programa]: '))

    if aluno == 999:
        break
    
    if aluno < qtd_cadastros and aluno >= 0:
        print('-'*10, end= '< ')
        print(boletim[aluno][0], end= ' >')
        print('-'*10)
        print('NOTA 1 - {}'.format(boletim[aluno][1]))
        print('NOTA 2 - {}'.format(boletim[aluno][2]))
        print('MÉDIA - {}'.format(boletim[aluno][3]))
        print('-'*30)

        sleep(5)
    else:
        print('Escolha inválida!! tente novamente...\n')


