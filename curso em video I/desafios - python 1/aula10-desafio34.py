'''
    Escreva um programa que pergunte o
salário de um funcionário e calcule o
valor do seu aumento

Para salários superiores a R$1.250,00,
calcule um aumento de 10%.

Para os inferiores ou iguais, o aumento
é de 15%.
'''
sal = float(input('Digite seu salário: R$'))
aumento = 0

if sal > 1250:
    aumento = 1250 * 0.10
    print(f'Salário: R${sal:.2f} \nc/ aumento: R${sal+aumento:.2f}')
else:
    aumento = 1250 * 0.15
    print(f'Salário: R${sal:.2f} \nc/ aumento: R${sal+aumento:.2f}')