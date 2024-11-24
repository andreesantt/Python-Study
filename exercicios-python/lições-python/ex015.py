d = int(input('Quantos dias alugados: '))
km = float(input('Quilômetros percorridos: '))
p = ( d * 60 ) + (km * 0.15)
print('O total a pagar é de R${}'.format(p))