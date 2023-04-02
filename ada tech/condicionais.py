idade = 20

if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor idade.')

'''
Imprimir 'Aprovado" caso o estudante tenha uma média
superior ou igual a 7, e 'Reprovado', caso a média seja
inferior a 7.
'''

nota1 = float(input('Insira sua primeira nota: '))
nota2 = float(input('Insira sua segunda nota: '))
nota3 = float(input('Insira sua terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
presenca = int(input('Qual a porcentagem da sua presença? '))

if media >= 7 and presenca >= 70:
    print('Aprovado! \nMédia: {:.1f}'.format(media))
elif media >= 5 and presenca >= 50:
    print('Recuperação.')
else:
    print('Reprovado. \nMédia: {:.1f}'.format(media))