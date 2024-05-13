med = 0
hom = ''
ida_hom = 0
fem = 0
mul = 0
for x in range(4):
    nom = input('Digite o nome da {}° pessoa: '.format(x+1)).capitalize()
    ida = int(input('Digite a idade da {}° pessoa: '.format(x+1)))
    sex = input('Digite o sexo da {}° pessoa (m = masculino, f = feminino): '.format(x+1)).lower()
    if ida > ida_hom and sex == 'm':
        ida_hom = ida
        hom = nom
    if ida < 20 and sex == 'f':
        mul += 1
        fem += 1
    elif sex == 'f':
        fem += 1
    med += ida
if hom != '':
    print('O nome do homem mais velho é {}.'.format(hom))
else:
    print('Só há mulheres no grupo')
if mul != 0:
    print('Há {} mulher(es) com menos de 20 anos.'.format(mul))
elif fem == 0:
    print('Não há mulheres no grupo.')
else:
    print('Não há nenhuma mulher com menos de 20 anos.')
print('A média das idades é de {} anos.'.format(round(med/4)))
