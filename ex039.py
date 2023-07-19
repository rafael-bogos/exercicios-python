from datetime import date
atual = date.today().year
sexo = int(input('Digite (1) para Homem e (2) para mulher: '))
if(sexo == 1):
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
    if idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print(f'ainda faltam {saldo} anos para o alistamento')
        ano = atual + saldo
        print(f'Seu alistamento será em {ano}')
    elif idade > 18:
        saldo = idade -18
        print(f'Você já deveria ter se alistado há {saldo} anos')
        ano = atual - saldo
        print(f'Seu alistamento foi em {ano}')
elif(sexo == 2):
    print('Mulher NÃO é permitido fazer alistamento!')
else:
    print('ERRO!')