#Crie um programa que leia algo pelo teclado e mostre na tela o
#seu tipo primitivo e todas as informações possíveis sobre ela.
a = input("Digite algo: ")
print(type(a))
print(a.isupper(), ",", a.isalpha(), ",", a.isalnum(), ",", a.isnumeric())