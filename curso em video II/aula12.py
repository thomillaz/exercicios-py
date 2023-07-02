nome = str(input('Qual é seu nome? '))

if nome == 'Kamilla':
    print('Que nome bonito!')
elif nome == 'Ana' or nome == 'Carlos':
    print('Que nome interessante!')
else:
    print('Seu nome é legal!')

print('Tenha um bom dia, {}!'.format(nome))
print(f'Tenha um bom dia, {nome}!')