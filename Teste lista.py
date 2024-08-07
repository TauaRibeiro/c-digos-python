# As listas são mutáveis.
num = [1, 6, 4, 8, 0, 9]
print(num)
num[2] = 3
print(num)
# Insere um elemento no final da lista.
num.append(7)
# Insere um elemento em determinada posição (index, elemento)
num.insert(0, 9)
print(num)
# Organiza a lista. A função reverse inverte a organização.
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
# ''' Elimina um elemento da lista em determinada posição. Caso não haja um parâmetro,
# será eleminado o último elemento da lista.'''
num.pop(2)
num.pop()
print(num)
# Elimina a primeira ocorrência do elemento da lista.
num.remove(9)
print(num)
lista = []
# '''for x in range(0, 5):
#    lista.append(input('Digite algo: '))
# print(lista)
# Quando uma lista é igualada a outra, qualquer alteração feita em uma irá ocorrer na outra.
# Caso queira fazer uma cópia dos valores de uma lista deve-se fazer assim b = a[:]
a = [2, 3, 4, 7]
b = a
# b = a[:]
b[2] = 8
print(f'A lista "a" é {a}')
print(f'A lista "b" é {b}')
