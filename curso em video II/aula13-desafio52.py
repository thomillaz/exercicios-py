'''
    Faça um programa que leia um número inteiro e diga
se ele é ou não um número primo.
'''
num = int(input('Digite um número: '))
tot = 0

for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m')
        tot += 1
    else:
        print('\033[31m')
    print(f'{i}', end=' ')

if tot > 2:
    print(f'\n{num} não é primo.')
else:
    print(f'\n{num} é primo.')