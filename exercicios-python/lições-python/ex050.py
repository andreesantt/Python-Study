# Programa que lê seis números inteiros e mostre a soma se forem pares;
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c} valor inteiro: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} números PARES  e a soma foi {soma}')