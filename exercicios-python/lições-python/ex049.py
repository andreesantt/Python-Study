# Refazer desafio 09 com laço for
from time import sleep
print('=-'*25)
escolha_usuario = int(input('Digite um número para ver sua taboada: ')) #Usuário digita número para ver a tabuda
for t in range(escolha_usuario-1, 11): # Laoço de repetição
    multiplique = escolha_usuario * t # Fórmula para a tabuada
    sleep(0.25)
    print(f'{escolha_usuario} x {t} = {multiplique}')
print('=-'*25)