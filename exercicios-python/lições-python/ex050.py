# Programa que lê seis números inteiros e mostre a soma se forem pares;
soma = 0
for num in range(1, 7):
    numpar = int(input('Digite um número inteiro: '))
    soma += numpar
if soma % 2:
    print(f'A soma dos números pares digitados são {soma}')