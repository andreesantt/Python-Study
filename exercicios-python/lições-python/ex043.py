#Leia peso e altura usuário e calcule IMC e mostre sua situação atual
peso_usuario = float(input('Digite seu peso: '))
altura_usuario = float(input('Digite sua altura: '))
alt2 = altura_usuario ** 2
imc = peso_usuario / alt2
print(f'Seu índice de massa corporal é {imc:.2f}, de acordo com os dados fornecidos\nE cálculo do seu IMC vamos identificar sua situação atual')
from time import sleep
print('AGUARDE...')
sleep(3)
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Você está no seu peso ideal')
elif 25 <= imc < 30:
    print('Você está em sobrepeso, precisa se cuidar')
elif 30 <= imc < 40:
    print('Obesidade, precisa cuidar da saúde')
else:
    print('Você está em obesidade mórbida, precisa urgente se cuidar')