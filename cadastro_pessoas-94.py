registro = list()
pessoa = dict()

total_cadastros = 0
media_idades = 0

achou  = False

while True:
    pessoa['nome'] = input('Digite o nome: ')
    pessoa['idade'] = int(input(f'Digite a idade de {pessoa["nome"]}: '))
    
    media_idades += pessoa['idade']

    while True:
        pessoa['sexo'] = input(f'Digite o sexo de {pessoa["nome"]} [M/F]: ').lower()
        
        if len(pessoa['sexo']) == 1 and pessoa['sexo'] in 'mf':
            break

        print('Opção inválida!! Tente novamente...')
    
    registro.append(pessoa.copy())

    pessoa.clear()

    total_cadastros += 1

    while True:
        continuar = input('Deseja continuar? [Sim/Nao]: ').lower()

        if continuar in 'simnãonao':
            break

        print('Opção inválida!! Tente novamente...')

    if continuar in 'nãonao':
        break

media_idades /= total_cadastros

print('=-'*30)
print(f'Foi cadastrado {total_cadastros} {'pessoa' if total_cadastros == 1 else 'pessoas'}.')
print(f'A média de idades é de {media_idades:.0f}.')

print('-'*30)
print('LISTA DE MULHERES')
for m in registro:
    if m['sexo'] == 'f':
        print(f'{"=>":>5} {m};')

        achou = True

if achou == False:
    print('Não há mulheres...')
print('-'*30)

achou = False

print('-'*30)
print('PESSOAS COM IDADE ACIMA DA MÉDIA')
for i in registro:
    if i['idade'] > media_idades:
        print(f'{"=>":>5} {i}:')

        achou = True
if achou == False:
    print('Não nimguém acima da média...')
print('-='*30)

