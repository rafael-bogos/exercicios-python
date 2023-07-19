print('-=-'*20)
print('Analisador de triângulos')
print('-=-'*20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Seguindo Segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triângulos ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ESÓSCELES!')
else:
    print('Os segmentos acima NÃO podem formar triângulos!')