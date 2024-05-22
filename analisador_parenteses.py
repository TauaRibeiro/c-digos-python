#incompleto
caracteres = []
expressao = (input('Digite uma expressão: '))
parenteses = 0

for x in range(0, len(expressao)):
    caracteres.append(expressao[x:x+1])

for x in caracteres:
    if x == '(':
        parenteses += 1
    elif x == ')' and parenteses >= 0:
        parenteses -= 1
    if parenteses <= 0:
        parenteses -= 1

if parenteses == 0:
    print('Expressão válida!!')
else:
    print('Expressão inválida!!')
