# Faça um programa que leia um número inteiro
# qualquer e mostre na tela a sua tabuada.
num = int(input('Digite um número: '))
i = 1
print('Tabuada de {}:'.format(num))
print('-' * 12)
print('{} X {:2} = {}'.format(num, i, num*i))
print('{} X {:2} = {}'.format(num, i+1, num*(i+1)))
print('{} X {:2} = {}'.format(num, i+2, num*(i+2)))
print('{} X {:2} = {}'.format(num, i+3, num*(i+3)))
print('{} X {:2} = {}'.format(num, i+4, num*(i+4)))
print('{} X {:2} = {}'.format(num, i+5, num*(i+5)))
print('{} X {:2} = {}'.format(num, i+6, num*(i+6)))
print('{} X {:2} = {}'.format(num, i+7, num*(i+7)))
print('{} X {:2} = {}'.format(num, i+8, num*(i+8)))
print('{} X {:2} = {}'.format(num, i+9, num*(i+9)))
print('-' * 12)