'''
    Crie um programa que leia o ano de nascimento de
sete pessoas. No final, mostre quantas pessoas ainda
não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date
atual = date.today().year
menor = 0
maior = 0
for i in range(0, 7):
    ano = int(input('Digite seu ano de nascimento: '))
    if atual - ano < 21:
        menor += 1
    else:
        maior += 1
print(f'{menor} pessoa(s) ainda são menores de idade, ', end='')
print(f'e {maior} já são maiores.')