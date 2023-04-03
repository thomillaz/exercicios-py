# Crie um programa que leia qunato dinheiro uma pessoa
# tem na carteira e mostre quantos doláres ela pode comprar.
# Considere: US$1,00 = R$3,27
din = float(input('Quanto dinheiro você possui na carteira? R$'))
dol = din/3.27
print('Você possui R${:.2f}, e pode comprar US${:.2f}.'.format(din,dol))