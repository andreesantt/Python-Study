#Valor do produto a ser pago com diferentes confições de pagamento
produto = float(input('Valor do produto: '))
print('Escolha condição de pagamento: ')
print('1 - A vista: + 10% Desconto\n2 - Á vista no cartão: + 5% desconto\n3 -2x Cartão: Preço normal\n4 -3x ou mais: 20% juros')
condição = int(input('Digite a condição de pagameno desejada: '))
if condição == 1:
    print((100 - 10) * produto)
elif condição == 2:
    print((100 - 5) / produto * produto)