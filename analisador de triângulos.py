S1 = float(input('Insira o primeiro segmento: ').replace(',', '.'))
S2 = float(input('Insira o segudo segmento: ').replace(',', '.'))
S3 = float(input('Insira o terceiro segmento: ').replace(',', '.'))
C1 = S1 + S2
C2 = S1 + S3
C3 = S2 + S3
if C1 > S3 and C2 > S2 and C3 > S1:
    print('Os seguimentos podem formar um triângulo!')
    if S1 == S2 == S3:
        print('O triângulo formado será um triângulo equilátero.')
    elif S1 != S2 != S3:
        print('O triângulo formado será um triângulo escaleno.')
    else:
        print('O triângulo formado será um triângulo isóceles.')
else:
    print('Os seguimentos não formam um triângulo!')
