#Programa que lê três comprimentos e mostra se forma um triangulo, se sim qual triângulo.
comprimento1 = int(input('Digite o primeiro comprimento: '))
comprimento2 = int(input('Digite o segundo comprimento: '))
comprimento3 = int(input('Digite o terceiro comprimento: '))
if comprimento1 + comprimento2 > comprimento3 and comprimento1 + comprimento3 > comprimento2 and comprimento2 + comprimento3 > 1:
    print('Parabéns, você formou um triângulo')
else:
    print('Você não pode formar um triângulo com esses dados')
if comprimento1 == comprimento2 == comprimento3:
    print('Este triangulo é Equilátero')
elif comprimento1 == comprimento2 != comprimento3 or comprimento1 == comprimento3 != comprimento2 or comprimento2 == comprimento3 != 1:
    print('O triangulo é isóceles')
else:
    print('O triangulo é Escaleno')