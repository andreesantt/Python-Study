#Escreva um programa que leia um valor em metros e o exiba convertido em
#centimetros e em milimetros.
print('Para converter metros em centimetros e milimetros basta digitar um número a baixo.')
m = float(input('Digite um valor: '))
c = m * 100
mm = c * 1000
print('O valor de {}m em centimetros é {}cm e em melimetros vale {}mm .'.format(m, c, mm))