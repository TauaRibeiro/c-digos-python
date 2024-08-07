# Tuplas são imutáveis, ou seja, não podem ser alteradas enquanto o código rodar.
# '''Você pode utilizar o comando del(nome_variável) para deletar uma variáve/ tupla,
# mas não um elemento'''
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print('-'*30)
print(lanche[0])
print('-'*30)
print(lanche[1:3])
print('-'*30)
print(lanche[0:])
print('-'*30)
contador = 11
for c in lanche:
    if contador < len(lanche):
        print(c, end=', ')
        contador += 1
    else:
        print(c)
print('-'*30)
for cont in range(0, len(lanche)):
    if cont < len(lanche):
        print(lanche[cont], end=', ')
    else:
        print(lanche[cont])
print(sorted(lanche))
print('-'*30)
a = (7, 2, 3)
b = (4, 5, 2, 7)
c = a + b
print(c)
print('-'*30)
print(c.index(2))
print('-'*30)
print(c.index(2, 5))
