'''
    Faça um programa que leia três números
e mostre qual é o maior e qual é o menor.
'''
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
maior = 0
menor = 0

if num1 > num2 and num2 < num3:
    print(f'Maior número: {num1} \nMenor número: {num2}')
