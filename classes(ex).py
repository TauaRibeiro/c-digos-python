class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def passar_canal(self, botao):
        if botao == '+':
            print('Aumentar canal')
        elif botao == '-':
            print('Diminuir Canal')



controle = ControleRemoto('preto', '10 cm', '2 cm', '2 cm')

print(controle.cor)
controle.passar_canal('+')

controle2 = ControleRemoto('cinza', '12 cm', '2 cm', '2 cm')

print(controle2.cor)
controle2.passar_canal('-')
