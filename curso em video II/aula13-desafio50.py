'''
    Desenvolva um programa que leia seis números int
e mostre a soma apenas daqueles que forem pares. Se o
valor for ímpar, desconsidere-o.
'''
num = 0
soma = 0

for i in range(1, 7):
    num = int(input(f'Digite o {i} valor: '))
    if num % 2 == 0:
        soma += num
    

print(f'Soma dos números: {soma}')