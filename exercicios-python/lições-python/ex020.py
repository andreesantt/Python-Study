import random
n1 = input('Aluno 01: ')
n2 = input('Aluno 02: ')
n3 = input('Aluno 03: ')
n4 = input('Aluno 04: ')
lista = [n1, n2, n3, n4]
ordem = random.shuffle(lista)
print(lista)

