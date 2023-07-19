name = int(input('Informe um numero: '))
num = str(name)

'''u = name // 1 % 10
d = name // 10 % 10
c = name // 100 % 10
m = name // 1000 % 10'''

print(f'Analisando o numero {name}')
print(f'Unidade: {num[-1]}')
print(f'Dezena: {num[-2]}')
print(f'Centena: {num[-3]}')
print(f'Milhar: {num[0]}')