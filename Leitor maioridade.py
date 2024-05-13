from datetime import date
ano = date.today().year
men = 0
mai = 0
for x in range(7):
    nas = int(input('Digite o ano de nascimento da {}° pessoa: '.format(x+1)))
    if ano - nas < 21:
        men += 1
    else:
        mai += 1
if men == 0:
    print('Todas as 7 pessoas são de maior.')
elif mai == 0:
    print('Todas as 7 pessoas são de menor.')
else:
    print('Das 7 pessoas {} são de maior e {} são de menoridade.'.format(mai, men))
