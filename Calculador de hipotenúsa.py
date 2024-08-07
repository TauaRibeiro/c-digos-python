from math import hypot
CA = float(input('Insira a medida do cateto adjecente: '))
CO = float(input('Insira a medida do cateto oposto: '))
print('A hipotenúsa será de {:.2f}'.format(hypot(CA, CO)))
