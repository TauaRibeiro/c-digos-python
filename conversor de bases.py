num = int(input('Digite um número inteiro: '))
print('Digite o número da base de conversão desejada:')
ba = input('1- Binário;\n2- Octal;\n3- Hexadecimal\ninput: ')
if ba == '1':
    numc = bin(num)
    x = 'binário'
elif ba == '2':
    numc = oct(num)
    x = 'Octal'
else:
    numc = hex(num)
    x = 'Hexadecimal'
print('A conversão do número {} para {} será:\n{}'.format(num, x, numc[2:]))
