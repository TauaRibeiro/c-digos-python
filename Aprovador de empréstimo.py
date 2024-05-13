val = float(input('Insira o valor da casa: ').replace(',', '.'))
sal = float(input('Insira o seu salário: ').replace(',', '.'))
ano = int(input('Insira quantos anos irá pagar: '))
pres = val/(ano*12)
if pres <= sal*1.30:
    print('Parabéns! O seu empréstimo foi liberado.')
    print('Você deverá pagar \033[4;33m{}\033[m prestações no valor de \033[4;33mR${:.2f}\033[m'.format(ano*12, pres))
else:
    print('\033[4;31mSinto muito, mas o empréstimo foi negado!!')
