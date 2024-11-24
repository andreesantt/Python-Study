#Faça um programa que leia a largura de uma parede em metros, calcule
#a sua área e a quantidade de tinta necessária para pintá-la, sabendo que
#cada litro de tinta, pinta uma área de 2m².
L = float(input('Largura da parede: '))
A = float(input('Altura da parede: '))
R = (L * A)
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(L, A, R))
print('Para pintar essa parede, você precisá de {}l'.format(R / 2))