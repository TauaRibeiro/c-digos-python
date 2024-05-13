from time import sleep
n1 = float(input('Digite um número:\n').replace(',', '.'))
n2 = float(input('Digite mais um número:\n').replace(',', '.'))

while True:
    escolha = int(input('''\nEscolha uma das opções no menu:
[1] Somar;
[2] Multiplicar;
[3] Maior;
[4] Escolher novos números;
[5] Finalizar programa;
Digite o número da sua escolha:\n'''))
    if escolha == 1:
        print('A soma dos números dá {}.'.format(n1+n2))
        sleep(2)
    elif escolha == 2:
        print('A multiplicação dos números dá {}.'.format(n1*n2))
        sleep(2)
    elif escolha == 3:
        if n1 > n2:
            print('O maior número é {}'.format(n1))
            sleep(2)
        elif n1 < n2:
            print('O maior número é {}'.format(n2))
            sleep(2)
        else:
            print('Não há maior número.')
            sleep(2)
    elif escolha == 4:
        n1 = float(input('Digite um número:\n').replace(',', '.'))
        n2 = float(input('Digite mais um número:\n').replace(',', '.'))
    elif escolha == 5:
        break
    else:
        print('Por favor, digite um número do menu.')
        sleep(2)
print('---FIM---')
