from random import choice
jo = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura'}
com = choice([1, 2, 3])
pla = int(input('''Selecione a sua escolha
1- Pedra;
2- Papel;
3- Tesoura;
Insira o número da sua escolha: ''').strip())
print('''Você escolheu {};
O computador escolheu {};'''.format(jo[pla], jo[com]))
if com == 1 and pla == 2:
    print('Você venceu!!')
elif com == 1 and pla == 3:
    print('Você perdeu!!')
elif com == 2 and pla == 1:
    print('Você perdeu!!')
elif com == 2 and pla == 3:
    print('Você venceu!!')
elif com == 3 and pla == 1:
    print('Você venceu!!')
elif com == 3 and pla == 2:
    print('Você perdeu')
else:
    print('Empate')
