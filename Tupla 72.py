numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
numero = int(input('Digite um número de 0 à 10: '))
while numero not in range(0, 11):
    numero = int(input('Tente novamente. Digite um número de 0 à 10: '))
print(f'Você digitou o número {numeros[numero]}.')
