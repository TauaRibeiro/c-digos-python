import datetime
ano = int(input('Digite o seu ano de nascimento: '))
alist = int(datetime.date.today().year)
if alist - ano < 18:
    print('Você ainda irá se alistar ao serviço militar.')
    print('Ainda falta {} ano(os) para realizar o alistamento'.format(18-(alist - ano)))
elif alist - ano == 18:
    print('Já está na hora de se alistar!!!')
else:
    print('Já passou da hora de você se alistar!!!')
    print('Você está {} ano(os) atrasado!!!'.format((alist - ano)-18))
