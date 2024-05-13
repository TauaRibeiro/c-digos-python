fra = input('Digite uma frase: ').strip()
afra = fra.lower().split()
afra = ''.join(afra)
com = (len(afra))//2+1
ini = 0
fim = (len(afra))-1
p = 1
for c in range(0, com):
    x = afra[ini]
    y = afra[fim]
    if x != y:
        p = 0
    ini += 1
    fim -= 1
if p == 1:
    print('A frase "{}" é um palíndromo'.format(fra))
else:
    print('A frase "{}" não é um palíndromo.'.format(fra))
