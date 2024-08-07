V = int(input('Qual o valor original do produto?'))
T = 1-(int(input('Qual o valor do desconto?')))/100
D = round(V*T, 2)
print('O produto com o desconto custará {}R$'.format(D))
