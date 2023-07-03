'''
    Faça um programa que mostre na tela uma contagem
regressiva para o estouro de fotos de artifício, indo
de 10 até 0, com uma pausa de 1 segundo entre eles.
'''
from time import sleep
print('{:=^40}'.format(' Fogos de artifício '))
for i in range(10, 0, -1):
    print(i)
    sleep(1)
print('FIIIIIIIIIIIIiiii...')
sleep(1)
print('POOOOOOOM')