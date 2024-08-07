num1 = float(input('Digite o primeiro número: ').replace(',', '.'))
num2 = float(input('Digite o segundo número: ').replace(',', '.'))
num3 = float(input('Digite o terceiro número: ').replace(',',  '.'))
if num1 >= num2 and num1 > num3:
    print('O maior número é {}'.format(num1))
    if num2 >= num3:
        print('O menor número é {}'.format(num3))
    else:
        print('O menor número é {}'.format(num2))
elif num2 > num1 and num2 >= num3:
    print('O maior número é {}'.format(num2))
    if num1 <= num3:
        print('O menor número é {}'.format(num1))
    else:
        print('O menor número é {}'.format(num3))
elif num3 >= num1 and num3 > num2:
    print('O maior número é {}'.format(num3))
    if num1 <= num2:
        print('O menor número é {}'.format(num1))
    else:
        print('O menor número é {}'.format(num2))
else:
    print('Não existe maior ou menor número, pois todos são iguais')
