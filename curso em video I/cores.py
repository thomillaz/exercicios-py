'''
    --- Cores no Python ---

-> style: 0 none
          1 bold
          4 underline
          7 negative

-> text: 30 branco
         31 vermelho
         32 verde
         33 amarelo
         34 azul
         35 roxo
         36 ciano
         37 cinza

-> back: 40 branco
         41 vermelho
         42 verde
         43 amarelo
         44 azul
         45 roxo
         46 ciano
         47 cinza

\033[0;33;44m
'''
print('\033[4;30;45mOlá mundo!\033[m')
print('\033[0;30;41mteste\033[m')
print('\033[4;33;44mteste\033[m')
print('\033[1;35;43mteste\033[m')
print('\033[30;42mteste\033[m')
print('\033[mteste\033[m')
print('\033[7;30mteste\033[m')