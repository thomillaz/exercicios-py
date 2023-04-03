# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite seu salário: R$'))
desco = salario * 0.15
salarioAumento = salario + desco
print('Seu salário era de R${:.2f}, mas com aumento de 15%, agora é R${:.2f}'.format(salario, salarioAumento))