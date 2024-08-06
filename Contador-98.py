from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1

    if passo == 0:
        passo = 1

    print(f'Contagem de {inicio} à {fim} de {passo} em {passo}')
    if inicio > fim:
        while fim <= inicio:
            print(inicio, end= ' ', flush= True)
            sleep(1)

            inicio -= passo

    else:
        while fim >= inicio:
            print(inicio, end= ' ', flush= True)
            sleep(1)

            inicio += passo
    
    print('FIM!')


print('=-'*30)
contador(1, 10, 1)
print('=-'*30)
contador(10, 0, 2)
print('=-'*30)
print('Agora é sua vez de personalizar a contagem!')

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

print('=-'*30)
contador(inicio, fim, passo)
