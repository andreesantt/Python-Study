from random import randint
itens = ('Pedra', 'Papel', 'Tesoura') #Itens a serem escolhidos
computer = randint(0, 2) #Ecolha do computador
print('=-'*15)  
print('Vamos jogar Jokempô ? ')
print('''Qual sua escolha:
[ 00 ] PEDRA
[ 01 ] PAPEL
[ 02 ] TESOURA''')
player = int(input('Faça sua escolha: '))
from time import sleep
# Agguarda mostrar resultados
print('AGUARDE...')
sleep(3)
# Exibe escolhas
print(f'Você escolheu {itens[player]}')
print(f'Eu escolhi {itens[computer]}')
# Situações onde computador e jogador escolhem os mesmos itens.
if player == computer:
    print('EMPATE')
#Situações computador vence.
elif (computer == 0 and player == 2) or (computer == 1 and player == 0) or (computer == 2 and player == 1):
    print('Que pena pra você. Eu venci')
#Situações onde jogador vence
elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print('Que sorte! Você venceu')
# Finaliza o jogo
sleep(3)
print('=-'*15)