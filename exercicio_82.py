numeros = []
pares = []
impares = []

while True:
    numeros.append(int(input('Digite um número: ')))
    
    while True:

        escolha = input('Deseja continuar? [S/N]:').lower()
        if escolha in 'simnãonao':
            break
        print('Escolha inválida, tente novamente...')

    if escolha in 'nãonao':
        break
    

for x in numeros:
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)

print('-='*50)
print(f'A lista completa é {numeros}')
print(f'A lista de números pares é {pares}')
print(f'A lista de números ímpares é {impares}')
