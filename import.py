# Para arredondar um número usando o .format() utiliza-se {:.xf}, sendo x o número de casas decimais desejadas.
# import- importa tudo de uma biblioteca
# from xx import x1,x2,... - importa uma função específica da biblioteca
from math import sqrt, floor
num = int(input('Insira um número: '))
raiz = sqrt(num)
print('A raíz de {} é: {:.2f}'.format(num,floor(raiz)))
