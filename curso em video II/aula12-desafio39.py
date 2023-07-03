'''
    Faça um programa que leia o ano de nascimento de um
jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar;
- Se é a hora de se alistar;
- Se já passou do tempo do alistamento.

    Seu programa também deverá mostrar o tempo que
falta ou que passou do prazo.
'''
from datetime import date

genero = str(input('Qual seu gênero?\nH - homem\nM - mulher\n---> '))

if genero == 'H':
    ano = int(input('Insira seu ano de nascimento: '))
    atual = date.today().year
    idade = atual - ano
    difer = idade - 18

    print(f'Você tem {idade} anos.')

    if idade == 18:
        print('É a hora de se alistar.')
    elif idade > 18:
        print(f'Já passou {difer} anos do tempo de alistamento.')
    else:
        difer = difer * -1
        print(f'Falta {difer} anos para se alistar.')
elif genero == 'M':
    print('Você não precisa cumprir serviço militar obrigatório.')
else:
    print('Resposta inválida. Tente Novamente.')