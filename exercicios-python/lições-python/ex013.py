#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
#salário com 15% de aumento.
n1 = float(input('Digite aqui seu salário: '))
n2 = (15/100) * n1
n3 = n1 + n2
print('O seu salário com 15% de aumento passa a ser: {:.2f}.'.format(n3))