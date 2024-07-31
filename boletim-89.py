#ainda a ser terminado

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

print('='*30)
print('Número    Nome        Média')
for x in range(0, qtd_cadastros):
    print(f'{x}    {boletim[x][0]}')

