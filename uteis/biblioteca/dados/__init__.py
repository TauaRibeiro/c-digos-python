def leia_real(mensagem = ''):
    """Função que lê um valor monetário.

    Args:
        mensagem (str, optional): Mensagem que será mostrada no input. Defaults to ''.

    Returns:
        (str): Irá retornar o input do usuário apenas quando o usuário digitar um valor monetário.
    """
    while True:
        valido = True

        entrada = input(mensagem).strip()

        entrada = entrada.replace(',', '.')
        
        if len(entrada) == 0:
            print(f'ERRO!! \"{entrada}\" é um valor inválido!!')

            valido = False

        for caracter in entrada:
            if caracter.isnumeric() == False and caracter != '.': 
                    print(f'ERRO!! \"{entrada}\" é um valor inválido!!')

                    valido = False

                    break

        if valido:
            return float(entrada)


def leia_inteiro(mensagem = ''):
    """Função responsável por ler valores inteiros.

    Args:
        mensagem (str, optional): Mensagem de input. Defaults to ''.

    Returns:
        (int): Irá retornar um valor inteiro quando o usuário inserir um valor inteiro.
    """
    while True:
        valido = True

        entrada = input(mensagem).strip()

        for caracter in entrada:
             if not caracter.isnumeric():
                valido = False

                print(f'ERRO!! \"{entrada}\" é um valor inválido!!')

                break
        
        if valido:
            return int(entrada)
