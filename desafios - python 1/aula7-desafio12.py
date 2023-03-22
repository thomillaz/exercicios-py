# Faça um programa que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o valor do produto: '))
desco = preco * 0.05
precoFinal = preco - desco
print('O valor do produto é R${:.2f}, e com desconto de 5% fica R${:.2f}.'.format(preco, precoFinal))