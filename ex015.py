km = float(input('Quantos KM o carro rodou? '))
dias = int(input('Por quantos dias você alugou? '))
y = (km * 0.15) + (dias * 60)
print(f'O valor total a se pagar pelo carro é de: R${y:.2f}')