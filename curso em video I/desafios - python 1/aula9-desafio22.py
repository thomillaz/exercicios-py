'''
    Crie um programa que leia o nome completo
de uma pessoa e mostre:
> o nome com todas as letras maiúsculas;
> o nome com todas as letras minúsculas;
> quantas letras ao todo (sem considerar espaços);
> quantas letras tem o primeiro nome.
'''
nome = str(input('Digite seu nome completo: '))
dividido = nome.split()
nomeTodo = len(nome) - nome.count(' ')

print(f'Analisando seu nome: \nEm maiúsculas: {nome.upper()}')
print(f'Em minúsculas: {nome.lower()}')
print(f'Seu nome completo possui {nomeTodo} letras.')
print(f'Seu primeiro nome possui {len(dividido[0])} letras.')