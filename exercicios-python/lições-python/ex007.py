#Desenvolva um programa que leia as duas notas de um aluno, calcule
#e mostre a sua média
n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite outra nota: '))
m = n1 + n2
r = m / 2
print('A média das notas {:.1f} e {:.1f}, vale {:.1f}.'.format(n1, n2, r))