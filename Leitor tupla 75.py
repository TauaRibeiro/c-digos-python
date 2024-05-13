tupla = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
cont_9 = 0
posi_3 = -1
par = False
for x in tupla:
    if x == 9:
        cont_9 += 1
for y in range(0, 4):
    if tupla[y] == 3:
        posi_3 = y+1
        break
print('O valor 9 apareceu {} {}'.format(cont_9, 'vezes.' if cont_9 != 1 else 'vez.'))
print('O valor 3 apareceu {} '.format('em nenhuma posição.' if posi_3 == -1 else f'na {posi_3}°.'))
print('Os valores pares digitados foram: ', end=' ')
for z in tupla:
    if z % 2 == 0:
        print(z, end=' ')
