nome = input('Digite seu nome completo: ')
pri_nome = nome.split()[0]
letras_total = len(nome) - nome.count(' ')
print('''{}
{}
Tem {} letras
E o primeiro nome tem {} letras'''.format(nome.upper(), nome.lower(), letras_total, len(pri_nome)))
