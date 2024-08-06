def calcularBoletim(*notas, sit= False):
    """->Função responsável por gerar um boletim

    Args:
        notas(float): uma ou mais notas que serão usadas para calcular a média. (permite várias notas);
        sit (bool, optional): Indica se gostaria de mostrar a situação do aluno. Defaults to False;

    Returns:
        dict: retorna um dicionário que contém: total de notas, maior nota, menor nota, média, e situação(caso sit seja True);
    """
    boletim = dict()

    boletim['total'] = len(notas)
    soma = 0
    maior = menor = notas[0]
    
    for nota in notas:
        soma += nota

        if nota > maior:
            maior = nota
        
        if nota < menor:
            menor = nota
    
    boletim['maior'] = maior
    boletim['menor'] = menor
    boletim['média'] = soma/len(notas)
    
    if sit:
        if boletim['média'] > 7:
            boletim['situação'] = 'BOA'
        elif boletim['média'] < 5:
            boletim['situação'] = 'RUIM'
        else:
            boletim['situação'] = 'RAZOÁVEL'
        
    return boletim


boletim = calcularBoletim(3.5, 6)
print(boletim)