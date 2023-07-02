'''
    Escreva um programa para aprovar o empréstimo
bancário de uma casa. O programa vai perguntar o
valor da casa, o salário do comprador e em quantos
anos ele vai pagar.

    Calcule o valor da prestação mensal, sabendo
que ela não pode exceder 30% do salário ou então
o empréstimo será negado.
'''
valorCasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do salário do comprador: R$'))
ano = int(input('Digite em quantos anos irá pagar: '))
porcentagem = salario * (30/100)
parcela = (ano * 12)
preMensal = valorCasa / parcela

print(f'30% de R${salario:.2f} é R${porcentagem:.2f}')

if preMensal <= porcentagem:
    print(f'Valor da prestação mensal: R${preMensal:.2f}')
    print(f'Será pago em {ano} ano(s), em {parcela} parcela(s)')
else:
    print('Empréstimo negado. Saldo insuficiente.')