cont = 0
soma = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
if cont == 1:
    print(f'Você informou apenas {cont} número par')
else:
    print(f'Você informou {cont} números pares e a soma foi {soma}')