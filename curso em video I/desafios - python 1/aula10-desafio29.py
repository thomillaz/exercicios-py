'''
    Escreva um programa que leia a velocidade
de um carro.
    Se ele ultrapassar 80Km/h, mostre uma mensagem
dizendo que ele foi multado.
    A multa vai custar R$7,00 por cada Km acima
do limite.
'''
velocidade = int(input('Qual a velocidade do seu carro? '))
multa = 0

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Velocidade acima do permitido!')
    print(f'Multa: R${multa:.2f}')
else:
    print('Boa viagem!')