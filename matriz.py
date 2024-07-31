matriz = [[], [], []]

soma_pares = soma_coluna3 = 0

for x in range(0, 3):
    for y in range(0, 3):
        matriz[x].append(int(input(f'Digite o um valor para [{x}, {y}]: ')))

        if matriz[x][y] % 2 == 0:
            soma_pares += matriz[x][y]

        if y == 2:
            soma_coluna3 += matriz[x][y]

maior_linha2 =  matriz[1][0]

print('=-'*30)

for x in matriz:
    for y in x:
        print(f'[{y:^5}]', end= '')
    
    print()

for x in range(1, 3):
    if matriz[1][x] > maior_linha2:
        maior_linha2 = matriz[1][x]

print('=-'*30)
print(f'A soma de todos os elementos pares é {soma_pares};')
print(f'A soam de todos os elementos da coluna 3 é {soma_coluna3};')
print(f'O maior valor da segunda linha é {maior_linha2};')

