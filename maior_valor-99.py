from time import sleep


def maior(*numeros):
    maior = 0

    print('=-'*30)
    print('Analisando os valores passados...')
    if len(numeros) != 0:
        for numero in numeros:
            if numero > maior:
                maior = numero

            print(f'{numero}', end=' ', flush= True)

            sleep(1)
    
    print(f'{"Foi informado" if len(numeros) == 1 else "Foram informados"} {len(numeros)} {"valor" if len(numeros) == 1 else "valores"} ao todo.')
    print(f'O maior valor informado foi {maior}')

maior(2, 9, 4, 5, 7 , 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
