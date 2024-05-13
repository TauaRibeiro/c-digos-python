lista = []
maior = 0
posi_maior = []
menor = 0
posi_menor = []
for x in range(0, 5):
    lista.append(int(input(f'Digite um número para a {x+1}° posição: ')))
    if x == 0:
        maior = lista[0]
        menor = lista[0]
    else:
        if lista[x-1] > lista[x] and lista[x] < menor:
            menor = lista[x]
        if lista[x - 1] < lista[x] and lista[x] > maior:
            maior = lista[x]
for y in range(0, 5):
    if lista[y] == menor:
        posi_menor.append(y+1)
    if lista[y] == maior:
        posi_maior.append(y+1)
print(f'Você digitou os seguintes números {lista}')
print(f'O maior número é {maior}, e está nas posições {posi_maior}.')
print(f'O menor número é {menor}, e está nas posições {posi_menor}.')
