# A função censura irá receber dois parâmetros: Texto e Lista 
def censura (Texto, Lista) :
    # O for loop irá ver cada elemento da lista 'Lista' e irá atribuir a variavel x
    for x in Lista :
        # A if statment irá ver se x está contido em Texto, caso esteja irá rodar o que foi programado
        if x in Texto:
            y = x.replace(x," **** ")
            Texto = Texto.replace(x,y)
    # O 'return' irá atribuir como valor a variável texto
    return Texto

#Texto a ser censurado    
O_texto= input("digite o texto" )
#A lista de palavras que devem ser censuradas
Lista_de_censura = ["cu","idiota","merda","porra"]

print(censura( O_texto, Lista_de_censura)) 
#'''Essa função permite censurar uma palavra dentro de uma string'''
