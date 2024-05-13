print('=' * 30)
print('{:^30}'.format('CAIXA ELETRÔNICO'))
print('=' * 30)
saque = int(input('Quanto você gostaria de sacar? R$'))
nota_50 = nota_20 = nota_10 = 0
if saque >= 50:
    nota_50 = saque // 50
    saque = saque % 50
    print('Total de {} {} de R$50'.format(nota_50, 'cédulas' if nota_50 > 1 else 'cédula'))
    print('-' * 30)
if saque >= 20:
    nota_20 = saque // 20
    saque = saque % 20
    print('Total de {} {} de R$20'.format(nota_20, 'cédulas' if nota_20 > 1 else 'cédula'))
    print('-' * 30)
if saque >= 10:
    nota_10 = saque // 10
    saque = saque % 10
    print('Total de {} {} de R$10'.format(nota_10, 'cédulas' if nota_10 > 1 else 'cédula'))
if saque >= 1:
    print('Total de {} {} de R$1'.format(saque, 'cédulas' if saque > 1 else 'cédula'))
