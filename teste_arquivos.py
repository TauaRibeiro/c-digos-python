import sys

with open('Teste.txt', 'w', encoding= 'utf 8') as arquivo:
    arquivo.write('Olá mundo!!\n')



with open('Teste.txt', 'a', encoding= 'utf 8') as arquivo:
    arquivo.write('Este é um arquivo')



with open('Teste.txt', 'r', encoding= 'utf 8') as arquivo:
    texto = arquivo.readlines()

    for linha in texto:
        print(linha.replace('\n', ''))

