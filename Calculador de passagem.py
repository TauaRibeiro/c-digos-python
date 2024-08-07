dis = float(input('Insira a distância da viagem em Km: '))
if dis<=200:
    p = (dis*0.5)
else:
    p = (dis*0.45)
print('O preço da passagem será de {:.2f} R$'.format(p).replace('.',','))
