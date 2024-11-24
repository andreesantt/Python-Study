#Programa que lê três comprimentos e mostra se forma um triangulo, se sim qual triângulo.
t1 = int(input('Comprimento 01: '))
t2 = int(input('Comprimento 02: '))
t3 = int(input('Comprimento 03: '))
if t1 + t2 > t3 and t1 + t3 > t2 and t2 + t3 > t1:
    print('Paranbéns você conseguiu formar um triangulo ')
if t1 == t2 and t1 == t3 and t2 == t2:
    print('O triangulo é hequilatéro')
elif t1 == t2 != t3 or t1 == t3 != t2:
    print('O triângulo é Isóceles')
elif t1 != t2 and t1 != t3 or t2 != t3:
    print('O triângulo é Escaleno')
else:
    print('Você não conseguiu formar um triângulo')