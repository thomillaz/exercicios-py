'''
    Desenvolva um programa que leia o primeiro termo
e a razão de uma PA. No final, mostre os 10 primeiros
termos dessa progressão.
'''
termo = int(input('Digite um número: '))
razao = int(input('Digite o valor da razão: '))
decimo = termo + (10 - 1) * razao

for i in range(termo, decimo + razao, razao):
    print(f'{termo}', end=', ')
    termo += razao
