def fatorial(numero, show=False):
    """->Função que calcula o fatoria de um número;

    Args:
        numero (int): Número que será calculado o fatorial;
        show (bool, optional): Valor lógico que indica se irá mostrar ou não o cálculo. Defaults to False.

    Returns:
        int: Irá retornar o resultado do fatorial
    """
    resultado = 1

    for n in range(numero, 0, -1):
        if show == True:
            print(f'{n}', end=' ')

            if n == 1:
                print('=', end=' ')
            else:
                print('x', end=' ')

        resultado *= n
    
    return resultado

print(fatorial(7, show= False))
