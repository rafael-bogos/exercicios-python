Numero = float(input('Digite um numero qualquer: '))
resultado = Numero % 2
if resultado == 1:
    print(f'O numero {Numero:.0f}, é IMPAR')
else:
    print(f'O numero {Numero:.0f}, é PAR')