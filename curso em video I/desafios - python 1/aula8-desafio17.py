'''
    Faça um programa que leia o comprimento
do cateto oposto e do cateto adjacente de um
triângulo retângulo, calcule e mostre o
comprimento da hipotenusa.

---> Resolução matemática
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hi:.2f}.')
'''
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}.')