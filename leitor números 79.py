lista = []
while True:
    duplicado = False
    num = int(input('Digite um número: '))
    for x in lista:
        if num == x:
            duplicado = True
    if duplicado is True:
        print('Número duplicado, não irei adicionar...')
    else:
        lista.append(num)
        print('Valor adiconado com sucesso...')
    decisao = input('Deseja continuar [S/N]? ')
    while decisao not in 'SNsn':
        decisao = input('Por favor, tente novamente [S/N]: ')
    if decisao in 'Nn':
        break
lista = sorted(lista)
print('{}{}'.format('Os números digitados foram: ' if len(lista) > 1
                    else 'O número digitado foi:', lista))
