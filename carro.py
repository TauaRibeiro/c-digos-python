from uteis.biblioteca import dados

class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.tanque = 0


    def adicionar_combustivel(self, litros):
        if litros == 0:
            print('Quantidade inválida!!')
        else:
            self.tanque += litros

            print('Carro abastecido com sucesso!!')


    def andar(self, distancia):
        if distancia / self.consumo > self.tanque:
            distancia = self.consumo * self.tanque

        self.tanque -= distancia / self.consumo

        if self.tanque < 0:
            self.tanque = 0

        if self.tanque == 0:
            print('Você ficou sem gasolina na viagem!!')
            print(f'Mas conseguiu andar {distancia} Km.')
        else:
            print(f'Você andou {distancia} Km.')

        
    def mostrar_tanque(self):
        print(f'Você possui {self.tanque:.2f} L de gasolina.')
        
        if self.tanque == 0:
            print('Por favor reabasteça o carro.')


fusca = Carro(dados.leia_real('Digite o consumo (Km/L) do veículo: '))
finalizar = False

while not finalizar:
    print('Oque deseja fazer?')
    print('-'*30)
    print('1. Andar')
    print('2. Abastecer')
    print('3. Verificar tanque')
    print('4. Desligar.')
    print('-'*30)
    escolha = dados.leia_inteiro('Digite o número da opção desejada: ')
    
    print('=-'*30)
    match(escolha):
        case 1:
            if fusca.tanque == 0:
                print('Sem gasolina...')
            else:
                fusca.andar(dados.leia_real('Digite a distancia desejada: '))
        case 2:
            fusca.adicionar_combustivel(dados.leia_real('Digite a quantida de combustível a ser adicionada: '))
        case 3:
            fusca.mostrar_tanque()
        case 4:
            print('Desligando...')

            finalizar = True
        case _:
            print('Escolha inválida!! Tente novamente')
    
    print('=-'*30)
