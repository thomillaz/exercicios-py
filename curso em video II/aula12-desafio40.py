'''
    Crie um programa que leia duas notas de um aluno
e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''
nota1 = float(input('Insira sua nota: '))
nota2 = float(input('Insira sua outra nota: '))
media = (nota1 + nota2)/2

print(f'Nota 1: {nota1:.1f} | Nota 2: {nota2:.1f} | Média: {media:.1f}')

if media >= 7.0:
    print('APROVADO.')
elif 6.9 >= media >= 5.0:
    print('RECUPERAÇÃO.')
else:
    print('REPROVADO.')
