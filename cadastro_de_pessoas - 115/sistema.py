from biblioteca import dados
from modulo_gravacao_leitura import pessoa, mostrar_pessoas

cores = {'certo' : '\033[7;30;42m', 'errado' : '\033[4;31;40m','limpa' : '\033[m', 
         'amarelo' : '\033[0;33m', 'azul' : '\033[0;34m'}

while True:
    print('='*30)
    print(f'{'MENU PRINCIPAL':^30}')
    print(f'='*30)

    print(f'{cores["amarelo"]}1{cores["limpa"]}- {cores["azul"]}Cadastrar{cores["limpa"]};')
    print(f'{cores["amarelo"]}2{cores["limpa"]}- {cores["azul"]}Mostrar pessoas{cores["limpa"]};')
    print(f'{cores["amarelo"]}3{cores["limpa"]}- {cores["azul"]}Sair{cores["limpa"]};')
    decisao = dados.leia_inteiro(f'{cores["amarelo"]}Digite o número da opção desejada: {cores["limpa"]}')
    

