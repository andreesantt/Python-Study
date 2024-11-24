n1 = float(input('Digite a velocidade do carro: '))
n2 = (n1 - 80) * 7
if n1 <= 80:
    print('Velocidade permitida, parabéns: ')
else:
    print('A velocidade está acima do km permitido, você será multado')
    print('A multa será de {}'.format(n2))