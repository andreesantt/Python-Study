#Leia peso e altura usuário e calcule IMC e mostre sua situação atual
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso // (altura ** 2)
if 18.5 <= imc:
    print('seu IMC equivale a {}\nSegundo a Organização Mundial de Saúde\nVocê está \033[0;;41mABAIXO\033[;m do peso ideal'.format(imc))
elif imc >= 18.5 or imc <= 25:
    print('Seu IMC resuta em {}\nVocê está no seu peso \033[4;0;42mIDEAL\033[;m'.format(imc))
elif imc >= 25 or imc <= 30:
    print('Alerta de sáude\nSeu IMC está em {}\nVocê está com \033[4;0;46mSOBREPESO\033[;m'.format_map(imc))
else:
    30 <= imc or 40 <= imc:
        print('Alerta de saúde\nIMC em {}\nVocê está com \033[;;41mOBESIDADE\033;m'.format(imc))