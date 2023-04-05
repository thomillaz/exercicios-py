'''
 Crie um programa que leia um número Real qualquer
pelo teclado e mostre na tela a sua porção inteira.
'''
num = float(input('Digite um número real: '))
print(f'Número real: {num} \nPorção inteira: {num:.0f}')


'''
Outra resolução, utilizando módulos:

import math

num = float(input('Digite um número real: '))
print(f'Número real: {num} \nPorção inteira: {math.trunc(num)}')

-----> Outra solução:
print(f'Número real: {num} \nPorção inteira: {int(num)})
'''