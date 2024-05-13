num = int(input('Digite um número: '))
p = 0
for x in range(2, num):
    if num % x == 0:
        p = 1
if p == 0:
    print('O número {} é primo.'.format(num))
else:
    print('O número {} não é primo.'.format(num))
