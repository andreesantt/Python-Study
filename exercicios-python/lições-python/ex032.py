from datetime import date
ano = int(input('Em que ano você está? Coloque 0 para analisar o ano atual:  '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Você está em um ano Bissexto!!!')
else:
    print('Você não está em um ano Bissexto!!!')
