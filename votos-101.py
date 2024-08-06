from datetime import date


ano_atual = date.today().year


def validador(idade):
    """Função que irá informar se poderá votar

    Args:
        idade (int)-> idade do eleitor;

    Returns:
        'VOTO NEGADO'-> caso seja menor que 16 anos;
        'VOTO OPCIONAL'-> caso a idade esteja entre 16 e 17 anos ou seja maior que 70 anos;
        'VOTO OBRIGATÓRIO'-> caso nenhuma das condições sejam verdadeiras;
    """
    if idade < 16:
        return 'VOTO NEGADO'
    elif idade in [16, 17] or idade > 70:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'
    

ano_nascimento = int(input('Digite o ano em que nasceu: '))

print(f'Com {ano_atual - ano_nascimento} anos: {validador(ano_atual - ano_nascimento)}')

