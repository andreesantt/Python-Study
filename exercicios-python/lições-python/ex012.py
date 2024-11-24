#Faça um algoritmo que lei um preço de um produto e mostre o seu novo
#preço 5% de desconto.
n1 = float(input('Digite o o valor: '))
n2 = (5/100) * n1
n3 = n1 - n2
print('O valor {} com desconto passa a ser {:.2f}'.format(n1, n3))