V = int(input('Qual o valor original do salário?'))
T = 1+(int(input('Qual o valor do reajuste?')))/100
S = round(V*T, 2)
print('O salário com o reajuste será de {}R$'.format(S))
