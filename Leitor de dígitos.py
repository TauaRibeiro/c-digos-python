num = int(input('Insira um número entre 0 e 9999: '))
print('''Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}'''.format(num%10, num%100//10, num%1000//100, num//1000))

