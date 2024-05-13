produto = input('Digite o nome do produto: ')
preco = float(input('Digite o preço do produto R$ ').replace(',', '.'))
total = preco
contador = 0
menor_preco = preco
pro_barato = produto
while True:
    deci = ''
    if preco > 1000:
        contador += 1
    if preco < menor_preco:
        menor_preco = preco
        pro_barato = produto
    while deci != 's' and deci != 'n':
        deci = input('Deseja continuar? [S/N] ').lower()
    if deci == 'n':
        break
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: R$ ').replace(',', '.'))
    total += preco
print(f'''O total da compra foi de R${total:.2f}.
Temos {contador} produto(os) que custa(am) mais de R$ 1000,00.
O produto mais barato foi o/a {pro_barato.lower()}, custando {menor_preco}.''')
