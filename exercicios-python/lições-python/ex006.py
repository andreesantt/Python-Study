#Crie um algoritimo que leia um numero e mostre o seu dobro, o seu triplo
#e raiz quadrada.
r = float(input('Digite um número: '))
r2 = int(r**(1/2))
print('O dobro vale {}, o triplo vale {} e a raiz quadrada vale {}.'.format((r*2), (r*3), r2))