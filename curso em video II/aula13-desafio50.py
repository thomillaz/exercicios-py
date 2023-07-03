'''
    Desenvolva um programa que leia seis números int
e mostre a soma apenas daqueles que forem pares. Se o
valor for ímpar, desconsidere-o.
'''
num = int(0)
soma = int(0)

for i in range(1, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num
    

print(f'Soma dos números: {soma}')