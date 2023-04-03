'''print()
input()
len()
max()'''

def saudacao():
    print('Seja bem-vindo(a)(e)!')

saudacao()

# função com parâmetros
nome = str(input('Como se chama? '))
def saudacao(nome):
    print(f'Seja bem-vindo(a)(e), {nome}!')

saudacao(nome)

# função com retorno
def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)
print('O resultado da soma é: ', resultado)

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
resultado = calculadora(10, 20, '+')
print(resultado)