x = input('\033[4;31;40mDigite algo:\033[m ')
print(f'O tipo primitivo desse valor é: {type(x)}')
print(f'Tem letras? {x.isalpha()}')
print(f'Tem numeros? {x.isnumeric()}')
print(f'Tem Letra e numero? {x.isalnum()}')
print(f'Está em minúsculo? {x.islower()}')
print(f'Está em maiúsculo? {x.isupper()}')
print(f'É composto pos minúscula e maiúscula? {x.istitle()}')
print(f'Só tem espaço? {x.isspace()}')
