velo = int(input('Digite a velocidade do carro: '))
if velo>80:
    print('Você foi multado em {:.2f}R$.'.format((velo-80)*7).replace('.',','))
print('---FIM---')
