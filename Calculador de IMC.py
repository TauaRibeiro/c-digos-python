al = float(input('Qual a sua altura em M?\n').replace(',', '.'))
pe = float(input('Qual o seu peso em Kg?\n').replace(',', '.'))
IMC = pe/al**2
if IMC < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= IMC < 25:
    print('Peso ideal.')
elif 25 <= IMC < 30:
    print('Sobrepeso.')
elif 30 <= IMC < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
