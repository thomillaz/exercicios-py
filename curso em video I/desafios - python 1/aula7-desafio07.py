# Desenvolva um programa que leia as duas notas
# de um aluno, calcule e mostre sua média.
nota = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota + nota2) / 2
print('A nota média do aluno é {:.1f}.'.format(media))