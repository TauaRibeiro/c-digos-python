def leiaDinheiro(mensagem = ''):
    while True:
        valido = True

        entrada = input(mensagem).strip()

        entrada = entrada.replace(',', '.')
        
        if len(entrada) == 0:
            print(f'ERRO!! \"{entrada}\" é um preço inválido!!')

            valido = False

        for caracter in entrada:
            if caracter.isnumeric() == False and caracter != '.': 
                    print(f'ERRO!! \"{entrada}\" é um preço inválido!!')

                    valido = False

                    break

        if valido:
            break
        
    return float(entrada)