num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'Convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opção == 2:
    print(f'Convertido para OCTAL é igual a {oct(num)[2:]}')
elif opção == 3:
    print(f'Convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção invalida, Tente novamente!')