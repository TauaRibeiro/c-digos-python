from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = tupla[0]
menor = tupla[0]
for x in tupla:
    if x > maior:
        maior = x
    if x < menor:
        menor = x
print('Os valores sorteados foram: ', end=' ')
for y in range(0, 5):
    if y < 4:
        print(tupla[y], end=', ')
    else:
        print(tupla[y], end='.\n')
print(f'O maior número sorteado foi {maior}.')
print(f'O menor número sorteado foi {menor}.')
