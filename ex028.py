#Mini game Pyhon
from random import randint
from time import sleep

num = randint(0,5)
print('-=-'*20)
jogador = int(input('Vou pensar em um numero entre 0 e 5. Tente adivinhar... '))
print('-=-'*20)
print('PROCESSANDO...')
sleep(3)
print('-=-'*20)
if jogador == num:
    print('Parabéns você acertou!')
else:
    print(f'Você errou! O numero era {num} e não {jogador}')
