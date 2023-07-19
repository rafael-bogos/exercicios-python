from time import sleep
print('-=-'*20)
distancia = float(input('Qual é a distancia da sua viagem em Km: '))
print('-=-'*20)
print('CALCULANDO VALOR TOTAL...')
print('-=-'*20)
sleep(3)
if distancia <= 200:
    passagem = distancia*0.50
    print(f'A sua viagem vai estar custando R${passagem:.2f}')
else:
    passagemP = distancia*0.45
    print(f'A sua viagem vai estar custando R${passagemP:.2f}')