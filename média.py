N1 = float(input('Qual a primeira nota? ').replace(',', '.'))
N2 = float(input('Qual a segunda nota? ').replace(',', '.'))
N3 = float(input('Qual a terceira nota? ').replace(',', '.'))
M = (N1+N2+N3)/3
print('A média será {}'.format(round(M, 1)))
if M < 5:
    print('REPROVADO')
elif 5 < M < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
