from datetime import date

funcionario = dict()

funcionario['nome'] = input('Digite o nome do funcionário: ')
funcionario['idade'] = int(input('Digite o ano de nascimento: '))
funcionario['ctps'] = int(input('Digite o número da carteira de trabalho (0 não tem): '))

if funcionario['ctps'] != 0:
    funcionario['ano'] = int(input('Digite o ano de contratação: '))
    funcionario['salario'] = float(input('Digite o salário: R$ '))

    ano_atual = date.today().year

    aposentadoria = (35 - (ano_atual - funcionario['ano']))

    if aposentadoria < 0:
        aposentadoria = 0

    aposentadoria = ano_atual + aposentadoria - funcionario['idade']

    funcionario['aposentadoria'] = aposentadoria
    funcionario['idade'] =  ano_atual - funcionario['idade']

print('-='*30)

for c, v in funcionario.items():
    print(f'{c} tem o valor {v}')
