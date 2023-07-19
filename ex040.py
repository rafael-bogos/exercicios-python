n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
nota = (n1 + n2) / 2
if nota < 5.0:
    print('REPROVADO!')
elif nota >= 5 and nota < 7:
    print('RECUPERAÇÃO!')
else:
     print('APROVADO!')
print(f'Tirando {n1} e {n2} a média é {nota}')