times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Red bull bragantino',
         'Fluminense', 'Athlético-PR', 'Internacional', 'Fortaleza')
print('=-'*30)
print('Os times em ordem alfabética são:', end=' ')
times_ord = sorted(times)
for x in times_ord:
    if times_ord.index(x) < (len(times)-1):
        print(x, end=', ')
    else:
        print(x, end='.\n')
print('=-'*30)
print('Os 5 primeiros colocados são: ', end=' ')
for pri in range(0, 5):
    if pri < 4:
        print(times[pri], end=', ')
    else:
        print(times[pri], end='.\n')
print('=-'*30)
print('Os 4 últimos colocaos são: ', end=' ')
for ult in range(1, 5):
    if ult < 4:
        print(times[-ult], end=', ')
    else:
        print(times[-ult], end='.\n')
print('=-'*30)
print('O time Flamengo está na {}° posição'.format(times.index('Flamengo')+1))
print('=-'*30)
