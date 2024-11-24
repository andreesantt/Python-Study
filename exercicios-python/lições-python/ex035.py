print('-='*20)
print('Analisador de Triângulos')
n1 = int(input('Número 01: '))
n2 = int(input('Número 02: '))
n3 = int(input('Número 03: '))
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('Parabéns você formou um triângulo!!!')
else:
    print('Você não conseguiu formar um triângulo!!!')