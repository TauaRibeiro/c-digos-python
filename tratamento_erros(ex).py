try:
    a = int(input('Numerador: '))
    b = int(input('Numerados: '))
    r = a/b
except (ValueError, TypeError):
    print('Erro com o tipo de dado')
except ZeroDivisionError:
    print('Não é possível realizar divizão por zero!')
except KeyboardInterrupt:
    print('O usuário não digitou nada.')
except Exception as erro:
    print(f'O erro que ocorreu foi -> {erro.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre!!')