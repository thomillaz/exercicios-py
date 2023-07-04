'''
    Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''
peso = 0
maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input('Digite seu peso: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
             maior = peso
        elif peso < maior and peso < menor:
            menor = peso


print(f'O menor peso foi {menor:.1f}kg, e o maior foi {maior:.1f}kg')