ano = int(input('Insira um ano: '))
ano2 = ano
if ano%100==0:
    ano = ano/100
if ano%4==0:
    print('O ano {} é bissexto'.format(ano2))
else:
    print('O ano {} não é bissexto'.format(ano2))

