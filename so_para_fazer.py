from uteis.biblioteca import moeda, dados

preco = dados.leiaDinheiro('Digite o preço: R$ ')

moeda.resumo(preco, 80, 35)
