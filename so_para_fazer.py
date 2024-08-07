numeros = []

while True:
    numeros.append(int(input('Digite um número: ')))
    while True:
        decisao = input('Deseja continuar [S/N]: ').lower()
        if decisao in 'simnãonao':
            break
        print('Escolha inválida tente novamente...')
    if decisao in 'nãonao':
        numeros.sort(reverse= True)
        break

print(f'Foram digitados {len(numeros)};')
print(f'A lista de valores ordenada de forma decrescente é {numeros};')
print('O valor 5 {} na lista;'.format('está' if 5 in numeros else 'não está'))