#Programa que lê o ano de nascimento de um atleta e mostre sua categoria
ano = int(input('Digite seu ano de nascimento: '))
from datetime import date
idade = date.today().year - ano
if 0 <= idade <= 9:
    print('Você tem {} anos e sua categoria é \033[0;;44mMIRIM\033[;m'.format(idade))
elif 9 <= idade <= 14:
    print('Você tem {} anos e sua categoria é \033[0;;42mINFANTIL\033[;m'.format(idade))
elif 14<= idade <= 19:
    print('Você tem {} anos e sua categoria é \033[0;;45mJÚNIOR\033[;m'.format(idade))
elif 19<= idade <= 20:
    print('Você tem {} anos e sua categoria é \033[0;;43mSÊNIOR\033[;m'.format(idade))
else:
    print('Você tem {} anos e sua categoria é \033[0;;41mMASTER\033[;m'.format(idade))
