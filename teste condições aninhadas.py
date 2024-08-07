nome = input('Qual o seu nome? ').strip().capitalize()
if nome == 'Tauã':
    print('Que belo nome!')
elif nome == 'Enzo' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}{}{}'.format('\033[4;33m', nome, '\033[m'))
