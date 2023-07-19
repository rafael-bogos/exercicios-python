peso = float(input('Qual seu peso? (KG): '))
altura = float(input('Qual sua altura? (M): '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('\033[33mABAIXO DO PESO!\033[m')
elif imc >= 18.5 and imc < 25:
    print('\033[32mPESO IDEAL!\033[m')
elif imc >= 25 and imc < 30:
    print('\033[33mSOBRE PESO!\033[m')
elif imc >= 30 and imc < 40:
    print('\033[31mOBESIDADE!\033[m')
else:
    print('\033[7;31mOBESIDADE MÓRBIDA!\033[m')