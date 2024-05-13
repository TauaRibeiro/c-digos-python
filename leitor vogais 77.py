palavras = ('Mercado', 'Azeitona', 'Game Stick', 'PYTHON', 'Sérgio')
for letra in palavras:
    print(f'A palavra {letra} tem as vogais: ', end='')
    for x in range(0, len(letra)):
        letra = letra.lower()
        teste = letra[x] in 'aeiou'
        if teste is True:
            print(letra[x], end=' ')
