numero = int(input('Digite um numero: '))
cont = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
if cont == 2:
    print(f'\n\033[mO número {numero} Foi divisível {cont} vezes. É um número PRIMO')
else:
    print(f'\n\033[mO número {numero} NÃO é um numero PRIMO')