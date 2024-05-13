pre = float(input('Qual o valor do produto?\n').replace(',', '.'))
pa = input('''Qual será a forma de pagamento?
1- À vista dinheiro/cheque (10% de desconto);
2- À vista no cartão (5% de desconto);
3- 2x no cartão;
4- 3x ou mais no cartão (20% de juros)
Insira o número da forma desejada: ''')
if pa == '1':
    pre = str(round(pre*0.9, 2)).replace('.', ',')
    print('O preço final será de R${}.'.format(pre))
elif pa == '2':
    pre = str(round(pre*0.95, 2)).replace('.', ',')
    print('O preço final será de R${}.'.format(pre))
elif pa == '3':
    pre = str(round(pre/2, 2)).replace('.', ',')
    print('O preço final será 2 parcelas de R${}.'.format(pre))
else:
    qp = int(input('Quantas parcelas desejadas?\n'))
    par = str(round(pre/qp, 2)).replace('.', ',')
    pre = str(round(pre*1.20, 2)).replace('.', ',')
    print('O preço final será {} parcelas de R${}, totalizando R${}'.format(qp, par, pre))
