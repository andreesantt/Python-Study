import random
n1 = str(input('Aluno 01: '))
n2 = str(input('Aluno 02: '))
n3 = str(input('Aluno 03: '))
n4 = str(input('Aluno 04: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O escolhido para ir ao quadro foi: {}'.format(escolhido))