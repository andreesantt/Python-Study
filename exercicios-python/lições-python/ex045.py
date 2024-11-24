from random import choice
lista = ('Pedra', 'Papel', 'Tesoura') #Itens a serem escolhidos
computer = choice(lista) #Ecolha do computador
print('=-'*15)
print('Vamos jogar Jokempô ? ')
print('''Qual sua escolha:
[ 00 ] PEDRA
[ 01 ] PAPEL
[ 02 ] TESOURA''')
player = int(input('Faça sua escolha: '))
from time import sleep
print('AGUARDE...')
sleep(3)
#Situações onde computador e jogador escolhem os mesmos itens.
if computer and player == 0:
    print('EMPATE')
    if computer and player == 1:
        print('EMPATE')
        if computer and player == 2:
            print('EMPATE')
#Situações computador ganha.
elif computer == 0 and player == 2:
    print('Que pena pra você! Eu escolhi {}. Eu venci '.format(computer))
elif computer == 1 and player == 0:
    print('Que pena pra você! Eu escolhi {}. Eu venci '.format(computer))
elif computer == 2 and player == 1:
    print('Que pena pra você! Eu escolhi {}. Eu venci '.format(computer))
#Situações onde jogador vence
elif player == 0 and computer == 2:
    print('Que sorte! Eu escolhi {}. Você venceu'.format(computer))
elif player == 1 and computer == 0:
    print('Que sorte! Eu escolhi {}. Você venceu'.format(computer))
elif player == 2 and computer == 1:
    print('Que sorte! Eu escolhi {}. Você venceu'.format(computer))
sleep(3)
print('=-'*15)