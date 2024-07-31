caracteres = []
parenteses = 0

expressao = (input('Digite uma expressão: '))

for x in range(0, len(expressao)):
    caracteres.append(expressao[x:x+1])

for x in caracteres:
    if x == '(':
        parenteses += 1
    elif x == ')':
        if parenteses >= 1:
            parenteses -= 1
        else:
            parenteses -= 1
            break
        

if parenteses == 0:
    print('Expressão válida!!')
else:
    print('Expressão inválida!!')
