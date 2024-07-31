pessoas = list()
entrada = list()

menor_peso = maior_peso = total_cadastros = 0

while True:
    entrada.append(input('Digite o nome da pessoa a ser cadastrada: '))
    entrada.append(float(input(f'Digite o peso de {entrada[0]}: ')))

    if maior_peso == 0:
        maior_peso = menor_peso = entrada[1]
    elif entrada[1] > maior_peso:
        maior_peso = entrada[1]
    elif entrada[1] < menor_peso:
        menor_peso = entrada[1]
        
    pessoas.append(entrada[:])
    entrada.clear()

    total_cadastros += 1
    
    while True:
        continuar = (input('Deseja cadastrar mais uma pessoa? [Sim/Não]: ')).lower()

        if continuar in 'simnãonao':
            break
        
        print('Opção inválida!! Tente novamente...')
    
    if continuar in 'nãonao':
        break
       

print('-='*30)
print('No total {} {} {}'.format('Foram cadastradas' if total_cadastros > 1 else 'Foi cadastrada', total_cadastros, 'pessoas' if total_cadastros > 1 else 'pessoa'))

print(f'O maior peso foi {maior_peso} Kg. Peso de ', end= '')
for x in pessoas:
    if x[1] == maior_peso:
        print(f'[{x[0]}] ', end=' ')

print(f'\nO maior peso foi {menor_peso} Kg. Peso de ', end= '')
for x in pessoas:
    if x[1] == menor_peso:
        print(f'[{x[0]}] ', end=' ')

    