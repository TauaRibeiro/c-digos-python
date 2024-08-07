f = input('Digite uma frase: ').lower().strip()
in_f = f.split()
Q = f.count('a')
P = f.find('a')
U = f.rfind('a')
print('''
A letra "A" aparece {} vezes
A primeira aparição está na {}° posição
A última aparição está na {}° posição'''.format(Q, P+1, U+1))
