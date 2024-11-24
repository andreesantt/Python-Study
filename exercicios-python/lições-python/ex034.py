s = float(input('Digite seu salário atual: '))
if s >= 1250:
    print('Seu novo salário passa a ser R$ {:.2f}'.format(s + (s * 10 / 100)))
else:
    print('Seu novo salário será de R${:.2f}'.format(s + (s * 15 / 100)))