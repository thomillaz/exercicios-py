'''
    Crie um programa que faça o computador jogar
Jokenpô com você.
'''
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('''
0 - Pedra
1 - Papel
2 - Tesoura
Sua opção: '''))

if jogador >= 3:
    print('ERRO! Tente novamente.')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!')
    print(f'\nComputador jogou: {itens[computador]}')
    print(f'Você jogou: {itens[jogador]}\n')
    if computador == 0 == jogador or computador == 1 == jogador or computador == 2 == jogador:
        print('EMPATE!')
    elif computador == 1 and jogador == 0:
        print('Computador VENCEU!')
    elif computador == 2 and jogador == 0:
        print('Você VENCEU!')
    elif computador == 0 and jogador == 1:
        print('Você VENCEU!')
    elif computador == 0 and jogador == 2:
        print('Computador VENCEU!')