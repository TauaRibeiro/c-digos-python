brasil = list()
estado = dict()

for x in range(0, 3):
    estado['unidade federativa'] = input('Unidade federativa: ')
    estado['sigla'] = input('Sigla do estado: ')

    brasil.append(estado.copy())

for e in brasil:
    for c, v in e.items():
        print(f'{c}: {v}')

        