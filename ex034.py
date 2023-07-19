from time import sleep
salario = float(input('Qual é o seu salario? '))
print('-=-'*20)
print('CALCULANDO SALARIO ATUAL...')
print('-=-'*20)
sleep(3)
if salario <= 1250:
    val1 = salario * 0.15
    print(f'Você passará a ganhar agora R${val1 + salario:.2f}')
else:
    val2 = salario * 0.10
    print(f'Você passará a ganhar agora R${val2 + salario:.2f}')