import sys

with open('Teste.txt', 'r', encoding= 'utf 8') as arquivo:
    
    texto = arquivo.readlines()

    print(texto)

arquivo.close()
