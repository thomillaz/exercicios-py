# nome = input('Qual seu nome? ')
# print('Prazer em te conhecer, {:-^20}!'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(' Entre {} e {}: \n a soma é {} \n o produto é {} \n a divisão é {:.2f} \n a divisão inteira é {} \n a potência é {}'.format(n1, n2, s, m, d, di, e))