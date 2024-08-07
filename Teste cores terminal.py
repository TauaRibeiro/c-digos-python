cores = {'limpa': '\033[m', 'azul': '\033[34m',
         'amarelo': '\033[33m', 'pretobranco': '\033[7;40m'}
print('\033[7;35;44mOlá mundo\033[m')
print('{}Olá mundo{}'.format('\033[31;40;1m' , '\033[m'))
print('{}Olá mundo!{}'.format(cores['pretobranco'], cores['limpa']))
