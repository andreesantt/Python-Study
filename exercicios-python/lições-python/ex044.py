# Programa que calcula o valor a ser pago considerando condições de pagamento.
print('{:=^40}'.format(''' ANDRE'S STORE '''))
valor_produto = float(input('Digite o valor produto: R$ ')) # Usuário digita valor do produto a ser calculado.
print('''Escolha a forma de pagamento desejada: 
    [ 1 ] À vista: 
    [ 2 ] Crédito a vista: 
    [ 3 ] Parcelado 2x: 
    [ 4 ] Parcelado 3x ou mais''')
forma_pagamento = int(input('Digite a opção desejada: '))
if forma_pagamento == 1:
    total = valor_produto - (valor_produto * 10 / 100)
elif forma_pagamento == 2:
    total = valor_produto - (valor_produto * 5 / 100)
elif forma_pagamento == 3:
    total = valor_produto
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de {parcela} SEM JUROS')
elif forma_pagamento == 4:
    total = valor_produto + (valor_produto * 20 / 100 )
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print(f'Sua compra será parcelada em {totalparc}x de R${parcela:.2f} COM JUROS')
else:
    total = valor_produto
    print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE')
print(f'Sua compra de R${valor_produto:.2f}, vai custar R${total:.2f} no final')