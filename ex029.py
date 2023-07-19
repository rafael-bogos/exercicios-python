vel = int(input('A quantos KM você passou pelo radar?'))
if vel > int(80):
    m = vel - int(80)
    v = m * int(7)
    print(f'Você ultrapassou o limite permitido e pagara de multa R${v}')
else:
    print('Parabéns por ser responsavel!')