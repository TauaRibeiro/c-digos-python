from biblioteca import dados
from modulo_gravacao_leitura import pessoa, mostrar_pessoas

cores = {'certo' : '\033[7;30;42m', 'errado' : '\033[4;31;40m','limpa' : '\033[m', 
         'amarelo' : '\033[0;33m', 'azul' : '\033[0;34m'}

fim = False

while not fim:
    print('='*30)
    print(f'{'MENU PRINCIPAL':^30}')
    print(f'='*30)

    print(f'{cores["amarelo"]}1{cores["limpa"]}- {cores["azul"]}Cadastrar{cores["limpa"]};')
    print(f'{cores["amarelo"]}2{cores["limpa"]}- {cores["azul"]}Mostrar pessoas{cores["limpa"]};')
    print(f'{cores["amarelo"]}3{cores["limpa"]}- {cores["azul"]}Sair{cores["limpa"]};')
    print('-'*30)
    decisao = dados.leia_inteiro(f'{cores["amarelo"]}Digite o número da opção desejada: {cores["limpa"]}')

    match(decisao):
        case 1:
            usuario = pessoa(dados.leia_letras('Digite o nome do usuário: '), dados.leia_inteiro('Digite a idade da pessoa: '))

            usuario.cadastrar()
        case 2:
            mostrar_pessoas()
        case 3:
            fim = True
        case _:
            print(f'{cores["errado"]}Opção inválida!!Por favor tente novamente...{cores["limpa"]}')
