'''
    Desenvolva um programa que pergunte a distância
de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e
R$0,45 para viagens mais longas.
'''
dist = float(input('Qual a distância da sua viagem? '))
psgem = 0
# psgem = dist * 0.50 if dist <= 200 else dist * 0.50
if dist <= 200:
    psgem = dist * 0.50
else:
    psgem = dist * 0.45
print(f'O valor da passagem é R${psgem:.2f}')