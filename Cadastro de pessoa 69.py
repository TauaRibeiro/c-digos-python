contador = 1
cont_idade = cont_homem = cont_mulher = 0
sexo = deci = ''
while True:
    idade = int(input(f'Digite a idade da {contador}° pessoa: '))
    while sexo != 'm' and sexo != 'f':
        sexo = input(f'Digite o sexo da {contador}° pessoa [M/F]: ').lower()
    if idade > 18:
        cont_idade += 1
    if sexo == 'm':
        cont_homem += 1
    if sexo == 'f' and idade < 20:
        cont_mulher += 1
    while deci != 's' and deci != 'n':
        deci = input('Deseja continuar? [S/N] ').lower()
    if deci == 'n':
        break
    contador += 1
    sexo = ''
    deci = ''
print(f'Tem {cont_idade} pessoa(as) com mais de 18 anos.')
print(f'Tem {cont_homem} homem(ns) cadastrado(os).')
print(f'Tem {cont_mulher} mulher(es) cadastrada(as) com menos de 20 anos.')
