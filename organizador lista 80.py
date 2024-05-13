lista = []
for x in range(0, 5):
    num = int(input(f'Digite o {x+1}° número: '))
    if len(lista) < 1:
        lista.append(num)
    elif len(lista) < 2:
        if num >= lista[0]:
            lista.append(num)
        else:
            lista.insert(0, num)
    else:
        comprimento = len(lista)
        for y in range(0, comprimento-1):
            if num <= lista[y]:
                lista.insert(y, num)
                break
            elif num <= lista[y+1]:
                lista.insert(y+1, num)
                break
            elif num > lista[len(lista)-1]:
                lista.append(num)
                break
print(lista)
