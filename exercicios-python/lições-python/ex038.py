#Ler dois número e mostrar qual maior entre eles
n = int(input('Digite um número: '))
n2 = int(input(('Digite outro número: ')))
if n > n2:
    print('Muito bem, {} é maior que {}'.format(n, n2))
elif n < n2:
    print("Temos {} maior que {}".format(n2, n))
else:
    print('Os valores são iguais')