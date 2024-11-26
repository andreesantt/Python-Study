# Programa que calcula o valor a ser pago considerando condições de pagamento.
valor_produto = float(input('Digite o valor produto: R$ ')) # Usuário digita valor do produto a ser calculado.
forma_pagamento = ('À vista', 'Crédito a vista', 'Parcelado 2x', 'Parcelado 3x ou mais')
print('''Escolha a forma de pagamento desejada: 
    [ 00 ] À vista: 
    [ 01 ] Crédito a vista: 
    [ 02 ] Parcelado 2x: 
    [ 03 ] Parcelado 3x ou mais''')
dinheiro_avista = valor_produto - (valor_produto * 0.1) # À vista em dinheiro; 10% de desconto.
credito_avista = valor_produto - (valor_produto * 0.05) # Crédito a vista; 5% de desconto.
parcelado2x = valor_produto # Crédito parcelado em 2x; valor do produto original
parcelado3x = valor_produto + (valor_produto * 0.25) #Crédito parcelado em 3x ou mais; 25% de juros
usuario_escolhe = int(input('Digite a condição de pagamento desejada: '))
if usuario_escolhe == 0:
    print(f'Você escolheu {forma_pagamento[usuario_escolhe]}, portanto ganhou 10% de desconto e pagará R${dinheiro_avista:.2f}')
elif usuario_escolhe == 1:
    print(f'Você escolheu {forma_pagamento[usuario_escolhe]}, ganhou 5% de desconto e pagará R${credito_avista:.2f}')
elif usuario_escolhe == 2:
    print(f'Você escolheu {forma_pagamento[usuario_escolhe]}, portanto o valor do produto não sofrerá alteraçãoes e você pagará {parcelado2x}.')
elif usuario_escolhe == 3:
    print(f'Você escolheu {forma_pagamento[usuario_escolhe]}, o valor fo produto passa a ser {parcelado3x} pois sofre juros de 25%')