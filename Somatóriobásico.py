#'''Esse código descreve um somatório de limite inferior 0 e limite superior'''

numero = int(input("Digite um número"))
resultado= 0
while numero >= 1 :
    resultado= numero + resultado
    numero= numero - 1
print(resultado)
