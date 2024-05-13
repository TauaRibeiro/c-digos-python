lista = ('Pão', 5.40, 'Farinha', 6.80, 'Queijo', 30.00, 'Presunto', 32.80, 'Refrigerante', 7.00)
print('-'*50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('-'*50)
for x in lista:
    if type(x) is str:
        dis = 40-len(x)
        print('{}{}'.format(x, '.'*dis), end='R$ ')
    else:
        print('{:>5.2f}'.format(x))
print('-'*50)
