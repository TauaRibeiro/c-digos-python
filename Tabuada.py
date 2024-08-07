while True:
    num = int(input('Quer ver a tabuada de qual número? '))
    if num < 0:
        break
    print('------------------------------')
    for x in range(1, 11):
        print(f'{num} X {x} = {num*x}')
    print('-----------------------------')
print('programa TABUADA ENCERRADO. Volte sempre!')
