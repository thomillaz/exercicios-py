'''
    Faça um programa que leia o ano de nascimento de um
jovem e iforme, de acordo com sua idade>

- Se ele ainda vai se alistar ao serviço militar;
- Se é a hora de se alistar;
- Se já passou do tempo do alistamento.

    Seu programa também deverá mostrar o tempo que
falta ou que passou do prazo.
'''
ano = int(input('Insira seu ano de nascimento: '))
tempo = 2023 - ano
difer = tempo - 18

if tempo == 18:
    print('É a hora de se alistar.')
elif tempo > 18:
    print(f'Já passou {difer} anos do tempo de alistamento.')
else:
    difer = difer * -1
    print(f'Falta {difer} anos para se alistar.')