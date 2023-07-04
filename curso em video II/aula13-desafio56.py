'''
    Desenvolva um programa que leia o nome, idade e sexo
de 4 pesoas. No final do programa, mostre:

- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres têm menos de 20 anos
'''
soma_idade = 0
velho = 0
nome_velho = 0
idade_velho = 0
mulheres = 0

for i in range(1, 5):
    print(f'----- {i}ª pessoa -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    genero = str(input('Gênero (F/M): '))

    if idade > velho and genero == 'M':
        nome_velho = nome
        idade_velho = idade
    
    if idade < 20 and genero == 'F':
        mulheres += 1
    soma_idade += idade

print(f'''
A média de idade do grupo é de {soma_idade/4}
O homem mais velho, de {idade_velho} anos, se chama {nome_velho}
Entre as mulheres, {mulheres} são menores de 20 anos
''')