class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome.capitalize()
        self.idade = idade
    
    def cadastrar(self):
        try:
            with open('registro_pessoas.txt', 'r', encoding= 'utf 8') as arquivo:
                leitura = arquivo.readlines()
        except FileNotFoundError:
            leitura = []
        except Exception as erro:
            print(f'Erro -> {erro.__class__}')

        duplicado = False

        for linha in leitura:
            analise = linha.split(',')

            if self.nome == analise[0]:
                print('Não é possível cadastrar uma pessoa já existente...')

                duplicado = True

                break

        if not duplicado:
            with open('registro_pessoas.txt', 'a', encoding= 'utf 8') as arquivo:
                arquivo.write(f'{self.nome}, {self.idade}\n')

            print('Cadastrado com sucesso')


def mostrar_pessoas():
    print(f'{'NOME':<30}{'IDADE'}')
    with open('registro_pessoas.txt', 'r', encoding= 'utf 8') as arquivo:
        pessoas = arquivo.readlines()

        for linha in pessoas:
            linha.replace('\n', '')

            usuario = linha.split(',')

            print(f'{usuario[0]:<30}{usuario[1]}', end= '')

