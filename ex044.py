compra = float(input('Qual o valor da compra? R$'))
val = int(input('''FORMAS DE PAGAMENTO:
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x do cartão
[ 4 ] 3x ou mais no cartão
Qual a opção?'''))
if val == 1:
    total = compra - (compra * 10 / 100)
elif val == 2:
    total = compra - (compra * 5 / 100)
elif val == 3:
    total = compra
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
elif val == 4:
    total = compra + (compra * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f} COM JUROS')
else:
    total = compra
    print('Opção invalidade. Tente novamente!')
print(f'Sua compra de {compra:.2f} vai custar {total:.2f} no final.')