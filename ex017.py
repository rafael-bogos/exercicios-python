from math import hypot
x = float(input('Digite o cateto oposto: '))
y = float(input('Digite o cateto adjacente: '))
result = hypot(x, y)
print(f'A hypotenusa é igual a {result:.2f}')