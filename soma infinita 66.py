soma = 0
while True:
    num = int(input('Digite um número (999 = para): '))
    if num == 999:
        break
    soma += num
print('{:-^25}'.format('FIM'))