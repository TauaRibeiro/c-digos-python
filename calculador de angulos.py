from math import cos, sin, tan, radians
angu = radians(float(input('Insira um ângulo qualquer: ')))
sen = sin(angu)
cos = cos(angu)
tan = tan(angu)
print('O seno é {:.2f};\nO cosseno é {:.2f};\nA tangente é {:.2f};'.format(sen, cos, tan))
