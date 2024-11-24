#Crie um programa que leia quanto de dinheiro a pessoa tem na carteira e
#e mostre quantos dólares ela pode comprar. Considere: US=1.00 =R$ = 3.27
n1 = float(input('Digite o valor da sua carteira: '))
n2 = float(n1 / 3.27)
print('A conversão de {} para dólares vale {:.2f}'.format(n1, n2))