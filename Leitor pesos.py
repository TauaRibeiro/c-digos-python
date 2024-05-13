p = float(input('Digite o peso da 1° pessoa: ').replace(',', '.'))
men_peso = p
mai_peso = p
for x in range(4):
    p = float(input('Digite o peso da {}° pessoa: '.format(x+2)).replace(',', '.'))
    if p < men_peso:
        men_peso = p
    elif p > mai_peso:
        mai_peso = p
if mai_peso == men_peso:
    print('Todos possuem o mesmo peso.')
else:
    print('O maior peso é de {} Kg e o menor é de {} Kg.'.format(mai_peso, men_peso))
