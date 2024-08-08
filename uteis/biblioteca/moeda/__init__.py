def moeda(numero):
    """Formata um número para formatação monetária (real R$).

    Args:
        preco (float): Número a ser formatado.

    Returns:
        (str): Retorna uma string contendo o valor formatado.
    """
    formatado = (f'R$ {numero:.2f}').replace('.', ',')

    return formatado

def dobro(preco, formatacao= False):
    """Calcula o dobro de um preco.

    Args:
        preco (float/int): quantidade em dinheiro a ser dobrada.
        formatacao (bool, optional): indica se um valor será formatado para moeda ou não. Default to False.

    Returns:
        (float/int): retorna o dobro do preço original.
        (str): irá retorna o preco formatado caso a formatacao seja True.
    """
    novo_preco = preco*2

    if formatacao:
        novo_preco = moeda(novo_preco)

    return novo_preco

def metade(preco, formatacao= False):
    """Calcula a metade de um preco

    Args:
        preco (float/int): quantidade em dinheiro a dividida pela metade.
        formatacao (bool, opticiona): indica se um valor será formatado para moeda ou não. Default to False.


    Returns:
        (float): retorna a metade do preço original.
        (str): irá retornar o preco formatado caso a formatacao seja True.
    """
    novo_preco = preco / 2

    if formatacao:
        novo_preco = moeda(novo_preco)

    return novo_preco

def aumentar(preco, porcentagem, formatacao= False):
    """Aumenta o preço a partir de uma determinada procentagem.

    Args:
        preco (float/int): quantidade em dinheiro a ser aumentada.
        porcentagem (float/int, optional): porcentagem da quantida a ser aumentada. Default to False.

    Returns:
        (float): retorna o preço mais a porcentagem do aumento.
        (str): irá retorna o preco formatado caso a formatacao seja True.
    """
    novo_preco = preco * (1 + porcentagem/100)

    if formatacao:
        novo_preco = moeda(novo_preco)

    return novo_preco

def diminuir(preco, porcentagem, formatacao= False):
    """Diminui o preço a partir de uma determinada procentagem

    Args:
        preco (float/int): quantidade em dinheiro a ser diminuida
        porcentagem (float/int, optional): porcentagem da quantida a ser diminuida. Default to False

    Returns:
        (float): retorna o preço menos a porcentagem da diminuição
        (str): irá retorna o preco formatado caso a formatacao seja True.
    """
    novo_preco = preco * (1 - porcentagem/100)

    if formatacao:
        novo_preco = moeda(novo_preco)

    return novo_preco

def resumo(preco, por_aumento= 0, por_diminuicao= 0):
    """"Função responsável por mostrar um resumo total de um preço.

    Args:
        preco (float/int): Preço a ser analisado
        por_aumento (float/int, optional): Porcentagem em que o preço será aumentado. Defaults to 0.
        por_diminuicao (float/int, optional): Porcentagem em que o preço será diminuido. Defaults to 0.
    """
    print('-'*30)
    print(f'{'RESUMO DO VALOR':^30}')
    print('-'*30)
    print(f'Preço analisado: {moeda(preco):>10}')
    print(f'Dobro do preço: {dobro(preco, True):>10}')
    print(f'Metade do preço: {metade(preco,True):>10}')

    if por_aumento != 0:
        print(f'{por_aumento}% de aumento: {aumentar(preco, por_aumento, True):>10}')
    
    if por_diminuicao != 0:
        print(f'{por_diminuicao}% de redução: {diminuir(preco, por_diminuicao, True):>10}')

    print('-'*30)