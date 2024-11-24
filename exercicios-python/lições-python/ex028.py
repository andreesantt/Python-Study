from random import randint
from time import sleep
n1 = int(input('Digite um número: ')) #JOGADOR TENTA ADIVINHAR NÚMERO
n = randint(0, 5) #FAZ COMPUTADOR PENSAR EM UM NÚMERO
print('PROCESSANDO...')
sleep(3)
if n1 == n:
    print('-=-'*20)
    print('Parabéns você acertou!!!')
    print('-=-'*20)
else:
    print('-=-'*20)
    print('Que pena você errou ;-;')
    print('Número escolhido foi {}'.format(n))
    print('-=-'*20)