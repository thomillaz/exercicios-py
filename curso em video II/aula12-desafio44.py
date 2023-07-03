'''
    Elabore um programa que calcule o valor a ser pago
por um produto, considerando o seu preço normal e
condição de pagamento:

- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''
print('{:=^40}'.format(' Loja de Vênus '))
preco = float(input('Qual o valor do produto: R$'))
pgto = int(input('''
Escolha a forma de pagamento:
1 - À vista em dinheiro/cheque
2 - À vista no cartão
3 - Em até 2x no cartão
4 - 3x ou mais no cartão
Sua opção:  '''))

if pgto == 1:
    preco = preco - (preco * (10/100))
    print(f'\nValor de pagamento: R${preco:.2f}')
elif pgto == 2:
    preco = preco - (preco * (5/100))
    print(f'\nValor de pagamento: R${preco:.2f}')
elif pgto == 3:
    print(f'\nValor de pagamento: R${preco:.2f}')
elif pgto == 4:
    preco = preco + (preco * (20/100))
    print(f'\nValor de pagamento: R${preco:.2f}')
else:
    print('Opção inválida. Tente novamente')