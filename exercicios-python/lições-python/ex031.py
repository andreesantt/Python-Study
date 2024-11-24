n1 = float(input('Digite a distância em KM: '))
if n1 <= 200:
    p1 = n1 * 0.50
    print('O preço é de R${} por {}km rodados'.format(p1, n1))
else:
    p2 = n1 * 0.45
    print('A viagem mais longa fica R${} por {}km rodados.'.format(p2, n1))